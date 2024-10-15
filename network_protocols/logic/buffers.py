from abc import ABC, abstractmethod
from typing import Optional
from uuid import UUID, uuid4


class Packet:
    def __init__(self, owner_oid: UUID, receivers: list[UUID]):
        self._oid: UUID = uuid4()
        self._data: str = "Some data for sending will be here"
        self._owner_oid: UUID = owner_oid
        self._receivers: list[UUID] = receivers

    @property
    def receivers(self) -> list[UUID]:
        return self._receivers


class Message:
    def __init__(self, data: Packet):
        self._data: Packet = data
        self.next: Optional["Message"] = None

    @property
    def packet(self) -> Packet:
        """Returns the message data (packet)"""
        return self._data


class BaseBuffer(ABC):
    @abstractmethod
    def put(self, data: Message) -> None:
        ...

    @abstractmethod
    def pop(self) -> Optional[Message]:
        ...

    @property
    @abstractmethod
    def length(self) -> int:
        ...


class Queue(BaseBuffer):
    def __init__(self):
        self.head: Optional[Message] = None
        self.tail: Optional[Message] = None

    def put(self, data: Message) -> None:
        if self.head is None:
            self.head = data
            self.tail = data
        else:
            self.tail.next = data
            self.tail = data

    def pop(self) -> Optional[Message]:
        if self.head is None:
            return None

        data = self.head
        self.head = self.head.next

        return data

    @property
    def length(self) -> int:
        if self.head is None:
            return 0

        length = 1
        current = self.head

        while current.next is not None:
            length += 1
            current = current.next

        return length
