from network_protocols.utils.factories import flood_initializer
from network_protocols.nodes.base import BaseFloodGateway


def test_flood_initializer():
    nodes = flood_initializer(max_nodes_count=10, gateways_count=2, max_packets=5)

    assert len(nodes) == 12

    for node in nodes:
        if isinstance(node, BaseFloodGateway):
            assert node.buffer.length == 0

        assert node.buffer.length >= 0 or node.buffer.length <= 5


def test_flood_initializer_without_gateways():
    nodes = flood_initializer(max_nodes_count=10, gateways_count=0, max_packets=5)

    assert len(nodes) == 10

    for node in nodes:
        if isinstance(node, BaseFloodGateway):
            assert node.buffer.length == 0

        assert node.buffer.length >= 0 or node.buffer.length <= 5


# TODO: implement test for test_leach_initializer
def test_leach_initializer():
    ...
