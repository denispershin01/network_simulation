from network_protocols.logic.factories import initialize_nodes, initialize_packets
from network_protocols.logic.gui import FloodSimulation
from network_protocols.logic.nodes import BaseNode


def main() -> None:
    nodes: list[BaseNode] = initialize_nodes(max_nodes=10)
    initialize_packets(nodes=nodes, max_packets=5)

    simulation = FloodSimulation(nodes=nodes)
    simulation.start()


if __name__ == "__main__":
    main()
