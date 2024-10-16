import random
from network_protocols.logic.buffers import Message, Packet
from network_protocols.logic.nodes.base import BaseNode
from network_protocols.logic.nodes.node import Node
from network_protocols.settings.config import Config


def initialize_nodes(max_nodes: int) -> list[BaseNode]:
    nodes = [
        Node(
            pos_x=random.randint(0, Config.SCREEN_WIDTH),
            pos_y=random.randint(0, Config.SCREEN_HEIGHT),
            radius=100,
        ) for _ in range(max_nodes)
    ]

    for node in nodes:
        node.find_neighbors(nodes)

    return nodes


def initialize_packets(nodes: list[BaseNode], max_packets: int) -> None:
    for node in nodes:
        for _ in range(random.randint(0, max_packets)):
            node.buffer.put(
                Message(
                    data=Packet(owner_oid=node.oid),
                ),
            )
