from abc import ABC, abstractmethod
import pygame

from network_protocols.nodes.base import BaseNode, BaseNodeProps
from network_protocols.settings.config import Config


class BaseSimulation(ABC):
    @abstractmethod
    def start(self) -> None:
        ...


class FloodSimulation(BaseSimulation):
    def __init__(self, nodes: list[BaseNodeProps]):
        self._nodes: list[BaseNodeProps] = nodes
        self._screen: pygame.Surface = pygame.display.set_mode(
            size=(Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT),
        )
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
                    for node in self._nodes:
                        if isinstance(node, BaseNode):
                            node.change_position(max_x=800, max_y=600)
                            node.find_neighbors(self._nodes)
                            node.send_messages(fpr=Config.FPR)
                        else:
                            node.clear_buffer()

            self._screen.fill("#1F1F1F")
            self._clock.tick(Config.FPS)

            self._draw_text_on_center(
                text="Press any key to move nodes...",
                screen_width=Config.SCREEN_WIDTH,
                y_pos=25,
            )
            self._draw_nodes()

            pygame.display.flip()

        pygame.quit()

    def _draw_nodes(self) -> None:
        """Draws the nodes and lines between neighbors"""
        for node in self._nodes:
            color = (255, 255, 255) if isinstance(node, BaseNode) else (255, 0, 0)

            pygame.draw.circle(
                surface=self._screen,
                color=color,
                center=node.coordinates,
                radius=6,
            )

            for neighbor in node.neighbors:
                pygame.draw.line(
                    surface=self._screen,
                    color=color,
                    start_pos=node.coordinates,
                    end_pos=neighbor.coordinates,
                    width=2,
                )

    def _draw_text_on_center(self, text: str, screen_width: int, y_pos: int) -> None:
        """Draws text on the screen"""
        font = pygame.font.SysFont(None, 32)
        text = font.render(text, True, (255, 255, 255))
        text_rect = text.get_rect(center=(screen_width//2, y_pos))
        self._screen.blit(text, text_rect)
