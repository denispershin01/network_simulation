import logging
import sys

from network_protocols.utils.factories import initialize_nodes, initialize_packets
from network_protocols.gui.flood_simulation import FloodSimulation
from network_protocols.nodes.base import BaseNode
from network_protocols.settings.config import Config


logger = logging.getLogger(__name__)
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)


def flood_algorithm() -> None:
    nodes: list[BaseNode] = initialize_nodes(max_nodes_count=Config.MAX_NODES, gateways_count=Config.MAX_GATEWAYS)
    initialize_packets(nodes=nodes, max_packets=Config.MAX_PACKETS)

    simulation = FloodSimulation(nodes=nodes)
    simulation.start()


def leach_algorithm() -> None:
    logger.warning("Leach algorithm is not implemented yet")


if __name__ == "__main__":
    try:
        match sys.argv[1]:
            case "flood":
                flood_algorithm()
            case "leach":
                leach_algorithm()
            case _:
                raise IndexError
    except IndexError:
        logger.warning("Missing argument. Please provide the argument for specifying the simulation algorithm.")
