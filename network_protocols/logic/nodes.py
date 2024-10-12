import random
from uuid import UUID, uuid4


class Node:
    def __init__(self, pos_x: int, pos_y: int, radius: int = 25) -> None:
        self._oid: UUID = uuid4()
        self._pos_x: int = pos_x
        self._pos_y: int = pos_y
        self._radius: int = radius
        self._speed: int = 40
        self._neighbors: list["Node"] = list()
        # TODO: add buffer for storing messages

    @property
    def oid(self) -> UUID:
        """Returns the unique id of the current node"""
        return self._oid

    @property
    def neighbors(self) -> list["Node"]:
        """Returns the neighbors of the current node"""
        return self._neighbors

    @property
    def coordinates(self) -> tuple[int, int]:
        """Returns the coordinates of the current node"""
        return self._pos_x, self._pos_y

    def find_neighbors(self, nodes: list["Node"]) -> None:
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

    def change_position(self, max_x: int, max_y: int) -> None:
        """Changes the position of the current node"""
        self._pos_x += random.randint(-self._speed, self._speed)
        self._pos_y += random.randint(-self._speed, self._speed)

        self._validate_new_position(max_x=max_x, max_y=max_y)

    def _validate_new_position(self, max_x: int, max_y: int) -> None:
        """Validates the new position of the current node"""
        if self._pos_x < 0:
            self._pos_x = 0
        elif self._pos_x > max_x:
            self._pos_x = max_x

        if self._pos_y < 0:
            self._pos_y = 0
        elif self._pos_y > max_y:
            self._pos_y = max_y
