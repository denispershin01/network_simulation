from network_protocols.nodes.base import BaseLeachNode, BaseLeachStation


class LeachStation(BaseLeachStation):
    def clear_buffer(self) -> None:
        """Delete all packets from the buffer"""
        self.buffer.clear()

    def receive_messages(self) -> None:
        """Receive messages from the cluster head nodes"""
        # TODO: implement this method
        ...

    def find_neighbors(self, nodes: list[BaseLeachNode]) -> None:
        """Find each cluster head nodes"""
        if len(self.neighbors) > 0:
            self.neighbors.clear()

        for node in nodes:
            if isinstance(node, BaseLeachNode) and node.is_cluster_head:
                self.neighbors.append(node)
