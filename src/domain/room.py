from dataclasses import dataclass
from .room_type import RoomType

#Room represents an actual hotel room.
#each room has a room number and is assigned a RoomType.
@dataclass(frozen=True)
class Room:
    room_number: str         #floor + room (e.g., 301)
    room_type: RoomType      #either Standard, Deluxe, Suite

    def capacity(self) -> int:
        """
        Returns the maximum number of guests this room can hold
        delegates to RoomType for rule enforcement
        """
        return self.room_type.max_guests()

    def price_per_night(self) -> int:
        """
        Returns the rate for this room
        delegates to RoomType for price logic
        """
        return self.room_type.price()
