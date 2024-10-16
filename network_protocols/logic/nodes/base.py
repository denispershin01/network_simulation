from abc import ABC, abstractmethod
from uuid import UUID

from network_protocols.logic.buffers import BaseBuffer


class BaseNode(ABC):
    @abstractmethod
    def find_neighbors(self, nodes: list["BaseNode"]) -> None:
        ...

    @abstractmethod
    def change_position(self, max_x: int, max_y: int) -> None:
        ...

    @abstractmethod
    def send_messages(self, fpr: int) -> None:
        ...

    @property
    @abstractmethod
    def oid(self) -> UUID:
        ...

    @property
    @abstractmethod
    def neighbors(self) -> list["BaseNode"]:
        ...

    @property
    @abstractmethod
    def buffer(self) -> BaseBuffer:
        ...

    @property
    @abstractmethod
    def coordinates(self) -> tuple[int, int]:
        ...
