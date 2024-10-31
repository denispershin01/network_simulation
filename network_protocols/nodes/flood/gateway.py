from network_protocols.nodes.base import BaseFloodGateway, BaseNodeProps


class FloodGateway(BaseFloodGateway):
    def find_neighbors(self, nodes: list[BaseNodeProps]) -> None:
        """
        Находит соседей текущего узла.
        Перед поиском соседей он очищает список соседей.
        """
       

    def clear_buffer(self) -> None:
        """Очищение буфера"""
        self.buffer.clear()
