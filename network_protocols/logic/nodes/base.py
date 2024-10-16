from abc import ABC, abstractmethod
from uuid import UUID, uuid4

from network_protocols.logic.buffers import BaseBuffer, Queue
from network_protocols.settings.config import Config


class BaseNodeProps(ABC):
    def __init__(self, pos_x: int, pos_y: int, radius: int = 100) -> None:
        self._oid: UUID = uuid4()
        self._pos_x: int = pos_x
        self._pos_y: int = pos_y
        self._radius: int = radius
        self._neighbors: list[BaseNode] = list()
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

    def find_neighbors(self, nodes: list["BaseNodeProps"]) -> None:
        """
        Finds the neighbors of the current node.
        Before finding neighbors, it clears the list of neighbors.
        """
        if len(self._neighbors) > 0:
            self._neighbors.clear()

        center_x, center_y = self.coordinates

        for neighbor in nodes:
            if neighbor.oid == self.oid:
                continue

            x, y = neighbor.coordinates

            # NOTE: Formula for finding points in the circle radius:
            # (x - center_x)² + (y - center_y)² = radius²
            if (x - center_x) ** 2 + (y - center_y) ** 2 <= self._radius ** 2:
                self._neighbors.append(neighbor)


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
