import random
from network_protocols.logic.buffers import Message, Packet
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


def initialize_packets(nodes: list[BaseNode], max_packets: int) -> None:
    for node in nodes:
        for _ in range(random.randint(0, max_packets)):
            node.add_message_to_buffer(
                Message(
                    data=Packet(
                        owner_oid=node.oid,
                        receivers=node.neighbors,
                    ),
                ),
            )
