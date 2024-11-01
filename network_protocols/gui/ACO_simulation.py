import pygame

from network_protocols.gui.base import BaseSimulation
from network_protocols.nodes.ACO.node import ACONode
#from network_protocols.nodes.ACO.gateway import ACOGateway
from network_protocols.settings.config import Config


class ACOSimulation(BaseSimulation):
    def start(self) -> None:
        """Запуск симуляции"""
        pygame.init()
        pygame.display.set_caption('ACOSimulation')

        while self._is_running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self._is_running = False

                if event.type == pygame.KEYDOWN:
                    for node in self._nodes:
                            if isinstance(node, ACONode):
                                node.change_position(max_x=Config.SCREEN_WIDTH, max_y=Config.SCREEN_HEIGHT)
                                node.find_neighbors(self._nodes)
                                #node.send_ant()
                            else:
                                node.find_neighbors(self._nodes)

                    for _ in range(Config.FPR):
                        for node in self._nodes:
                            if isinstance(node, ACONode):
                                node.send_ant()
                            else:
                                node.clear_buffer()

            self._screen.fill("#1F1F1F")
            self._clock.tick(Config.FPS)

            self._draw_nodes()

            self._draw_text_on_center(
                text="Нажми что-нибудь, пожалуйста...",
                screen_width=Config.SCREEN_WIDTH,
                y_pos=25,
            )

            pygame.display.flip()

        pygame.quit()
