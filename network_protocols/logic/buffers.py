from abc import ABC, abstractmethod
from typing import Optional


class Message:
    def __init__(self, data: str):
        self._data: str = data
        self.next: Optional["Message"] = None


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
