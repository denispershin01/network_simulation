from network_protocols.logic.factories import initialize_packets
from network_protocols.logic.nodes import Node


def test_coordinates():
    node = Node(pos_x=10, pos_y=10)

    assert node.coordinates == (10, 10)


def test_non_neighbors():
    node = Node(pos_x=10, pos_y=10)
    node.find_neighbors([])

    assert len(node.neighbors) == 0


def test_find_neighbors():
    node = Node(pos_x=10, pos_y=10, radius=25)
    nodes = [
        Node(pos_x=0, pos_y=10),
        Node(pos_x=10, pos_y=0),
        Node(pos_x=35, pos_y=20),
        Node(pos_x=10, pos_y=-10),
    ]

    node.find_neighbors(nodes)

    assert len(node.neighbors) == 3


def test_clear_neighbors():
    node = Node(pos_x=10, pos_y=10)
    neighbors = [
        Node(pos_x=0, pos_y=10),
        Node(pos_x=10, pos_y=0),
        Node(pos_x=35, pos_y=20),
        Node(pos_x=10, pos_y=-10),
    ]

    node.find_neighbors(neighbors)
    node.find_neighbors([])

    assert len(node.neighbors) == 0


def test_send_messages():
    nodes = [
        Node(pos_x=10, pos_y=10),
        Node(pos_x=0, pos_y=10),
        Node(pos_x=10, pos_y=0),
        Node(pos_x=35, pos_y=20),
        Node(pos_x=10, pos_y=-10),
    ]

    initialize_packets(nodes=nodes, max_packets=5)

    for node in nodes:
        node.send_messages(fpr=10)

        assert node.buffer.length == 0

        if len(node.neighbors):
            assert node.neighbors[0].buffer.length == 5
