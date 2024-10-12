from logic.gui import Simulation
from logic.nodes import Node


def main() -> None:
    nodes = [
        Node(pos_x=10, pos_y=10),
        Node(pos_x=30, pos_y=10),
        Node(pos_x=10, pos_y=30),
        Node(pos_x=30, pos_y=30),
    ]
    for node in nodes:
        node.find_neighbors(nodes)

    simulation = Simulation(nodes=nodes)
    simulation.start()


if __name__ == "__main__":
    main()
