from abc import ABC, abstractmethod
from uuid import UUID, uuid4

from network_protocols.buffers.base import BaseBuffer
from network_protocols.buffers.queue import Queue
from network_protocols.settings.config import Config


class BaseNodeProps(ABC):
    def __init__(self, pos_x: int, pos_y: int, radius: int = Config.NODE_RADIUS) -> None:
        self._oid: UUID = uuid4()
        self._pos_x: int = pos_x
        self._pos_y: int = pos_y
        self._radius: int = radius
        self._neighbors: list["BaseNodeProps"] = list()
        self._buffer: BaseBuffer = Queue()

    @property
    def oid(self) -> UUID:
        """Returns the unique id of the current node"""
        return self._oid

    @property
    def neighbors(self) -> list["BaseNodeProps"]:
        """Returns the neighbors of the current node"""
        return self._neighbors

    @property
    def buffer(self) -> BaseBuffer:
        """Returns the buffer of the current node"""
        return self._buffer

    @property
    def coordinates(self) -> tuple[int, int]:
        """Returns the coordinates of the current node"""
        return self._pos_x, self._pos_y

    @abstractmethod
    def find_neighbors(self, nodes: list["BaseNodeProps"]) -> None:
        ...


class BaseNode(BaseNodeProps):
    def __init__(self, pos_x: int, pos_y: int, radius: int = 100) -> None:
        self._speed: int = Config.NODE_SPEED
        self._energy: int = Config.NODE_ENERGY

        super().__init__(
            pos_x=pos_x,
            pos_y=pos_y,
            radius=radius * self._energy,
        )

    @abstractmethod
    def change_position(self, max_x: int, max_y: int) -> None:
        ...

    @abstractmethod
    def send_messages(self, fpr: int) -> None:
        ...


class BaseGateway(BaseNodeProps):
    @abstractmethod
    def clear_buffer(self) -> None:
        ...
