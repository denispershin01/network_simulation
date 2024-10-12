import pygame

from logic.nodes import Node


class Simulation:
    def __init__(self, nodes: list[Node]):
        self._nodes: list[Node] = nodes
        self._screen: pygame.Surface = pygame.display.set_mode((800, 600))
        self._clock: pygame.time.Clock = pygame.time.Clock()
        self._is_running: bool = True

    def start(self) -> None:
        """Starts the network simulation"""
        pygame.init()

        while self._is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._is_running = False

            self._screen.fill("#1F1F1F")
            self._clock.tick(60)

            self._draw_nodes()

            pygame.display.flip()

        pygame.quit()

    def _draw_nodes(self) -> None:
        """Draws the nodes and lines between neighbors"""
        for node in self._nodes:
            pygame.draw.circle(
                surface=self._screen,
                color=(255, 255, 255),
                center=node.coordinates,
                radius=6,
            )

            for neighbor in node.neighbors:
                pygame.draw.line(
                    surface=self._screen,
                    color=(255, 255, 255),
                    start_pos=node.coordinates,
                    end_pos=neighbor.coordinates,
                    width=2,
                )
