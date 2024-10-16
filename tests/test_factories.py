from network_protocols.logic.factories import initialize_nodes, initialize_packets


def test_nodes_factory():
    nodes = initialize_nodes(max_nodes_count=10)

    assert len(nodes) == 10


def test_packets_factory():
    nodes = initialize_nodes(max_nodes_count=10)
    initialize_packets(nodes=nodes, max_packets=5)

    for node in nodes:
        assert node.buffer.length >= 0 or node.buffer.length <= 5
