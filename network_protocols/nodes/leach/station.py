from network_protocols.nodes.base import BaseLeachNode, BaseLeachStation


class LeachStation(BaseLeachStation):
    def clear_buffer(self) -> None:
        """Delete all packets from the buffer"""
        self.buffer.clear()

    def find_neighbors(self, nodes: list[BaseLeachNode]) -> None:
        if len(self.neighbors) > 0:
            self.neighbors.clear()

        for node in nodes:
            if isinstance(node, BaseLeachNode) and node.is_cluster_head:
                self.neighbors.append(node)
