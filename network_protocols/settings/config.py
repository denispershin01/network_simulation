from typing import Final


class Config:
    SCREEN_WIDTH: Final[int] = 1024
    SCREEN_HEIGHT: Final[int] = 700
    FPS: Final[int] = 60
    FPR: Final[int] = 10
    MAX_PACKETS: Final[int] = 3
    MAX_NODES: Final[int] = 50
    MAX_GATEWAYS: Final[int] = 2
    NOISE_SIZE: Final[int] = 3
    NODE_ENERGY: Final[int] = 10
    NODE_RADIUS: Final[int] = 100
    STATION_RADIUS: Final[int] = 800
