from uuid import UUID, uuid4


class Node:
    def __init__(self, pos_x: int, pos_y: int, radius: int = 25) -> None:
        self._oid: UUID = uuid4()
        self._pos_x: int = pos_x
        self._pos_y: int = pos_y
        self._radius: int = radius
        self._neighbors: list[UUID] = list()
        # TODO: add buffer for storing messages

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
                self._neighbors.append(neighbor.oid)

    @property
    def coordinates(self) -> tuple[int, int]:
        """Returns the coordinates of the current node"""
        return self._pos_x, self._pos_y

    @property
    def neighbors(self) -> list[UUID]:
        """Returns the neighbors of the current node"""
        return self._neighbors

    @property
    def oid(self) -> UUID:
        """Returns the unique id of the current node"""
        return self._oid
