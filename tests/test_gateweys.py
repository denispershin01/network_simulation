from network_protocols.nodes.flood.gateway import FloodGateway


def test_non_neighbors():
    gateway = FloodGateway(pos_x=10, pos_y=10)
    gateway.find_neighbors([])

    assert len(gateway.neighbors) == 0


def test_find_neighbors():
    gateway = FloodGateway(pos_x=10, pos_y=10)
    nodes = [
        FloodGateway(pos_x=0, pos_y=10),
        FloodGateway(pos_x=10, pos_y=0),
        FloodGateway(pos_x=35, pos_y=20),
        FloodGateway(pos_x=10, pos_y=-10),
    ]

    gateway.find_neighbors(nodes)

    assert len(gateway.neighbors) == 4
