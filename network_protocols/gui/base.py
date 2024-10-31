from abc import ABC, abstractmethod

import pygame

from network_protocols.nodes.base import BaseFloodNode, BaseNodeProps, BaseACONode, BaseACOGateway, BaseFloodGateway
from network_protocols.settings.config import Config
from network_protocols.nodes.base import BaseLeachNode, BaseNodeProps, BaseLeachStation


class BaseSimulation(ABC):
    def __init__(self, nodes: list[BaseNodeProps]):
        self._nodes: list[BaseNodeProps] = nodes
        self._screen: pygame.Surface = pygame.display.set_mode(
            size=(Config.SCREEN_WIDTH, Config.SCREEN_HEIGHT),
        )
        self._clock: pygame.time.Clock = pygame.time.Clock()
        self._is_running: bool = True
        self._node_color: tuple[int, int, int] = (255, 255, 255)
        self._radius_color: tuple[int, int, int] = (66, 66, 66)
        self._gateway_color: tuple[int, int, int] = (255, 0, 0)
        self._line_color: tuple[int, int, int] = (255, 255, 255)

    @abstractmethod
    def start(self) -> None:
        ...

    def _draw_nodes(self) -> None:
        """Отрисовка радиусов узлов"""
        for node in self._nodes:
            if (node._energy > 0):
                if not isinstance(node,(BaseACOGateway,BaseFloodGateway)):
                    pygame.draw.circle(
                        self._screen,
                        self._radius_color,
                        node.coordinates,
                        node._radius,
                        1
                    )
        """Отрисовка узлов и линий между соседними объектами"""            
        for node in self._nodes:

            if isinstance(node, BaseLeachNode) and not node.is_cluster_head:
                color = self._node_color
            elif isinstance(node, BaseLeachNode) and node.is_cluster_head:
                color = self._gateway_color
            elif isinstance(node, BaseLeachStation):
                color = self._station_color

            elif isinstance(node, (BaseFloodNode,BaseACONode)):
                color = self._node_color
            else:
                color = self._gateway_color

            if (node._energy > 0):

                for neighbor in node.neighbors:
                    if isinstance(neighbor, (BaseACONode, BaseACOGateway)):
                        if not isinstance(node, BaseACOGateway):
                            pygame.draw.line(
                            surface=self._screen,
                            color=self._line_color,
                            start_pos=node.coordinates,
                            end_pos=neighbor.coordinates,
                            width = 1 + int(neighbor.pheromones_value()),
                            )
                    else:
                        pygame.draw.line(
                            surface=self._screen,
                            color=self._line_color,
                            start_pos=node.coordinates,
                            end_pos=neighbor.coordinates,
                            width=2,
                        )
                pygame.draw.circle(
                    surface=self._screen,
                    color=color,
                    center=node.coordinates,
                    radius=6,
                )
            else:
                pygame.draw.line(
                    self._screen,
                    color,
                    [node.coordinates[0] - 5,node.coordinates[1] + 5],
                    [node.coordinates[0] + 5,node.coordinates[1] - 5],
                    2
                )
                pygame.draw.line(
                    self._screen,
                    color,
                    [node.coordinates[0] - 5,node.coordinates[1] - 5],
                    [node.coordinates[0] + 5,node.coordinates[1] + 5],
                    2
                )

    def _draw_text_on_center(self, text: str, screen_width: int, y_pos: int) -> None:
        """Отрисовка текста на экране"""
        font = pygame.font.SysFont(None, 32)
        text = font.render(text, True, (255, 255, 255))
        text_rect = text.get_rect(center=(screen_width//2, y_pos))
        self._screen.blit(text, text_rect)
