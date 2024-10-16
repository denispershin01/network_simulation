from network_protocols.logic.nodes.gatewey import Gatewey


def test_non_neighbors():
    gatewey = Gatewey(pos_x=10, pos_y=10)
    gatewey.find_neighbors([])

    assert len(gatewey.neighbors) == 0


def test_find_neighbors():
    gatewey = Gatewey(pos_x=10, pos_y=10)
    nodes = [
        Gatewey(pos_x=0, pos_y=10),
        Gatewey(pos_x=10, pos_y=0),
        Gatewey(pos_x=35, pos_y=20),
        Gatewey(pos_x=10, pos_y=-10),
    ]

    gatewey.find_neighbors(nodes)

    assert len(gatewey.neighbors) == 4
