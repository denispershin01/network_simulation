import logging
import random
import math

from network_protocols.nodes.base import BaseACONode, BaseNodeProps
from network_protocols.settings.config import Config


logger = logging.getLogger(__name__)
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.INFO)

class ACONode(BaseACONode):
    def send_ant(self) -> None:
        """Выбирает привлекательного соседа и отправляет к нему муровья(сообщение)"""
        message = self.buffer.pop()
        if (message is not None) & (len(self.neighbors)>0):
            pheromones = [n._pheromones_bag for n in self.neighbors]
            selected_neighbor : BaseNodeProps
            if max(pheromones) <= 0:
                selected_neighbor = random.choice(self.neighbors) 
            else:
                exp_values = [math.exp((p/max(pheromones))/float(Config.NOISE_SIZE)) for p in pheromones]
                probabilities = [val/sum(exp_values) for val in exp_values]
                selected_neighbor = random.choices(self.neighbors,weights = probabilities, k=1)[0]

            if selected_neighbor.oid != message.packet.owner_oid:
                    selected_neighbor.buffer.put(message)
                    selected_neighbor._pheromones_bag += 0.1 #Сразу источаем феромоны
                    self._energy -= 0.01
    
    def send_messages(self, fpr: int = 5) -> None:
        """Отправляет сообщения соседям. Fpr - это ограничение на количество сообщений за раунд."""
        for _ in range(fpr):
            self.send_ant()

        logger.info("Buffer length for node %s after sending: %s\n", self.oid, self.buffer.length)

    def find_neighbors(self, nodes: list[BaseNodeProps]) -> None:
        """
        Находит соседей текущего узла.
        Перед поиском соседей он очищает список соседей.
        """
        if len(self._neighbors) > 0:
            self._neighbors.clear()

        center_x, center_y = self.coordinates

        for neighbor in nodes:
            if neighbor.oid == self.oid:
                continue

            x, y = neighbor.coordinates

            # NOTE: Formula for finding points in the circle radius:
            # (x - center_x)² + (y - center_y)² = radius²
            if (x - center_x) ** 2 + (y - center_y) ** 2 <= self._radius ** 2:
                if (neighbor._energy > 0):
                    self._neighbors.append(neighbor)

    def change_position(self, max_x: int, max_y: int) -> None:
        """Изменяет положение текущего узла. Количество энергии уменьшается на 0,1 при каждом перемещении."""
        self._energy -= 0.01
        self.pheromones_bag -= 0.05 #испарение феромона

        if self._energy <= 0:
            self._energy = 0
            return

        self._radius = self._energy * Config.NODE_RADIUS
        if(self._radius > Config.NODE_RADIUS):
            self._radius = Config.NODE_RADIUS

        self._pos_x += random.randint(-self._speed, self._speed)
        self._pos_y += random.randint(-self._speed, self._speed)

        self._validate_new_position(max_x=max_x, max_y=max_y)

    def _validate_new_position(self, max_x: int, max_y: int) -> None:
        """Проверяет новое положение текущего узла."""
        if self._pos_x < 0:
            self._pos_x = 0
        elif self._pos_x > max_x:
            self._pos_x = max_x

        if self._pos_y < 0:
            self._pos_y = 0
        elif self._pos_y > max_y:
            self._pos_y = max_y