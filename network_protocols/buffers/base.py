from abc import ABC, abstractmethod
from typing import Generic, Optional, TypeVar
from uuid import UUID, uuid4

MT = TypeVar("MT")


class BasePacket(ABC):
    def __init__(self, owner_oid: UUID) -> None:
        self._oid: UUID = uuid4()
        self._owner_oid: UUID = owner_oid

    @property
    def owner_oid(self) -> UUID:
        """Returns the owner of the packet"""
        return self._owner_oid


class BaseMessage(ABC, Generic[MT]):
    @property
    @abstractmethod
    def packet(self) -> MT:
        """Returns the message data"""
        ...


class BaseBuffer(ABC):
    @abstractmethod
    def put(self, data: BaseMessage) -> None:
        ...

    @abstractmethod
    def pop(self) -> Optional[BaseMessage]:
        ...

    @abstractmethod
    def clear(self) -> None:
        ...

    @property
    @abstractmethod
    def length(self) -> int:
        ...
