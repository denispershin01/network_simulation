from network_protocols.logic.factories import initialize_nodes, initialize_packets
from network_protocols.logic.nodes.base import BaseGateway


def test_nodes_factory_with_gateways():
    nodes = initialize_nodes(max_nodes_count=10, gateways_count=2)

    assert len(nodes) == 12


def test_nodes_factory_without_gateways():
    nodes = initialize_nodes(max_nodes_count=10, gateways_count=0)

    assert len(nodes) == 10


def test_packets_factory():
    nodes = initialize_nodes(max_nodes_count=10, gateways_count=2)
    initialize_packets(nodes=nodes, max_packets=5)

    for node in nodes:
        if isinstance(node, BaseGateway):
            assert node.buffer.length == 0

        assert node.buffer.length >= 0 or node.buffer.length <= 5
