from uuid import UUID, uuid4

class Pheromone:
    def __init__(self, owner_oid: UUID):
        self._oid: UUID = uuid4()
        self.value: float = 1