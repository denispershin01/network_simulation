from abc import ABC, abstractmethod
import pygame

from network_protocols.logic.nodes import BaseNode


class BaseSimulation(ABC):
    @abstractmethod
    def start(self) -> None:
        ...


class FloodSimulation(BaseSimulation):
    def __init__(self, nodes: list[BaseNode]):
        self._nodes: list[BaseNode] = nodes
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

                if event.type == pygame.KEYDOWN:
                    self._send_messages()
                    self._move_nodes()

            self._screen.fill("#1F1F1F")
            self._clock.tick(60)

            self._draw_text_on_center(
                text="Press any key to move nodes...",
                screen_width=800,
                y_pos=25,
            )
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

    def _move_nodes(self) -> None:
        """Move each node to their new position"""
        for node in self._nodes:
            node.change_position(max_x=800, max_y=600)
            node.find_neighbors(self._nodes)

    def _send_messages(self) -> None:
        """Sends the messages to the neighbors"""
        for node in self._nodes:
            node.send_messages(fpr=10)

    def _draw_text_on_center(self, text: str, screen_width: int, y_pos: int) -> None:
        """Draws text on the screen"""
        font = pygame.font.SysFont(None, 32)
        text = font.render(text, True, (255, 255, 255))
        text_rect = text.get_rect(center=(screen_width//2, y_pos))
        self._screen.blit(text, text_rect)
