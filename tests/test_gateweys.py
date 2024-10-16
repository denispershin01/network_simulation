from network_protocols.logic.nodes.gateway import Gateway


def test_non_neighbors():
    gateway = Gateway(pos_x=10, pos_y=10)
    gateway.find_neighbors([])

    assert len(gateway.neighbors) == 0


def test_find_neighbors():
    gateway = Gateway(pos_x=10, pos_y=10)
    nodes = [
        Gateway(pos_x=0, pos_y=10),
        Gateway(pos_x=10, pos_y=0),
        Gateway(pos_x=35, pos_y=20),
        Gateway(pos_x=10, pos_y=-10),
    ]

    gateway.find_neighbors(nodes)

    assert len(gateway.neighbors) == 4
