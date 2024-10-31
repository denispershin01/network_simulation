from network_protocols.nodes.base import BaseACOGateway, BaseNodeProps
from network_protocols.settings.config import Config

class ACOGateway(BaseACOGateway):


    def find_neighbors(self, nodes: list[BaseNodeProps]) -> None:
        """
        Находит соседей текущего узла.
        Перед поиском соседей он очищает список соседей.
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

    def clear_buffer(self) -> None:
        """Очищение буфера"""
        self.buffer.clear()