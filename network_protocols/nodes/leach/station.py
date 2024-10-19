from network_protocols.nodes.base import BaseNodeProps, BaseStation


class LeachStation(BaseStation):
    def clear_buffer(self) -> None:
        """Delete all packets from the buffer"""
        self.buffer.clear()

    def find_neighbors(self, nodes: list[BaseNodeProps]) -> None:
        # TODO: method will be find neighbors with HEAD_CLUSTER_NODE = True
        return super().find_neighbors(nodes)
