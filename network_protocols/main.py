from network_protocols.logic.factories import initialize_nodes
from network_protocols.logic.gui import FloodSimulation
from network_protocols.logic.nodes import BaseNode


def main() -> None:
    nodes: list[BaseNode] = initialize_nodes(max_nodes=10)
    simulation = FloodSimulation(nodes=nodes)

    simulation.start()


if __name__ == "__main__":
    main()
