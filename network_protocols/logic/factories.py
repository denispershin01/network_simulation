import random
from network_protocols.logic.nodes import BaseNode, Node


def initialize_nodes(max_nodes: int) -> list[BaseNode]:
    nodes = [
        Node(
            pos_x=random.randint(0, 800),
            pos_y=random.randint(0, 600),
            radius=100,
        ) for _ in range(max_nodes)
    ]

    for node in nodes:
        node.find_neighbors(nodes)

    return nodes
