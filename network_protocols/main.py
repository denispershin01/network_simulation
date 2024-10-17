from network_protocols.utils.factories import initialize_nodes, initialize_packets
from network_protocols.gui.flood_simulation import FloodSimulation
from network_protocols.nodes.base import BaseNode
from network_protocols.settings.config import Config


def main() -> None:
    nodes: list[BaseNode] = initialize_nodes(max_nodes_count=Config.MAX_NODES, gateways_count=Config.MAX_GATEWAYS)
    initialize_packets(nodes=nodes, max_packets=Config.MAX_PACKETS)

    simulation = FloodSimulation(nodes=nodes)
    simulation.start()


if __name__ == "__main__":
    main()
