from network_protocols.nodes.base import BaseLeachStation, BaseNodeProps


def move_nodes(nodes: list[BaseNodeProps], max_x: int, max_y: int):
    for node in nodes:
        if isinstance(node, BaseLeachStation):
            continue

        node.change_position(max_x=max_x, max_y=max_y)
