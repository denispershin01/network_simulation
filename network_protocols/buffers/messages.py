from typing import Optional
from uuid import UUID, uuid4


class Packet:
    def __init__(self, owner_oid: UUID):
        self._oid: UUID = uuid4()
        self._data: str = "Some data for sending will be here"
        self._owner_oid: UUID = owner_oid

    @property
    def owner_oid(self) -> UUID:
        """Returns the owner of the packet"""
        return self._owner_oid

    @property
    def receivers(self) -> list[UUID]:
        """Returns the receivers of the packet"""
        return self._receivers


class Message:
    def __init__(self, data: Packet):
        self._data: Packet = data
        self.next: Optional["Message"] = None

    @property
    def packet(self) -> Packet:
        """Returns the message data (packet)"""
        return self._data
