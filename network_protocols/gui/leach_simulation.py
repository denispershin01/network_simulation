import pygame

from network_protocols.gui.base import BaseSimulation
from network_protocols.nodes.base import BaseNode, BaseNodeProps
from network_protocols.settings.config import Config


class LeachSimulation(BaseSimulation):
    def __init__(self, nodes: list[BaseNodeProps]):
        super().__init__(nodes)
        self._station_color: tuple[int, int, int] = (0, 255, 0)
        self._cluster_separetor_color: tuple[int, int, int] = (75, 112, 97)

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
                            node.find_neighbors(self._nodes)
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
