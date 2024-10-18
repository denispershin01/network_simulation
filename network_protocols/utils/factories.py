import random
from network_protocols.buffers.messages import Message, Packet
from network_protocols.nodes.base import BaseGateway, BaseNode, BaseNodeProps
from network_protocols.nodes.flood.node import Node
from network_protocols.nodes.flood.gateway import Gateway
from network_protocols.settings.config import Config


def initialize_nodes(max_nodes_count: int, gateways_count: int) -> list[BaseNodeProps]:
    nodes = [
        Node(
            pos_x=random.randint(0, Config.SCREEN_WIDTH),
            pos_y=random.randint(0, Config.SCREEN_HEIGHT),
            radius=100,
        ) for _ in range(max_nodes_count)
    ]

    nodes.extend(
        Gateway(
            pos_x=random.randint(0, Config.SCREEN_WIDTH),
            pos_y=random.randint(0, Config.SCREEN_HEIGHT),
        ) for _ in range(gateways_count)
    )

    for node in nodes:
        node.find_neighbors(nodes)

    return nodes


def initialize_packets(nodes: list[BaseNode], max_packets: int) -> None:
    for node in nodes:
        if isinstance(node, BaseGateway):
            continue

        for _ in range(random.randint(0, max_packets)):
            node.buffer.put(
                Message(
                    data=Packet(owner_oid=node.oid),
                ),
            )
