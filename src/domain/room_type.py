from enum import Enum

#RoomType defines the three types of rooms available in the hotel,
#each with fixed pricing and guest capacity.
class RoomType(str, Enum):
    STANDARD = "Standard"
    DELUXE = "Deluxe"
    SUITE = "Suite"

    def price(self) -> int:
        """
        Returns the fixed nightly rate for each room type
        """
        return {
            RoomType.STANDARD: 100,
            RoomType.DELUXE: 200,
            RoomType.SUITE: 300,
        }[self]

    def max_guests(self) -> int:
        """
        Returns the maximum number of guests allowed per room type
        Standard: 2 guests max
        Deluxe: 3 guests max
        Suite: 4 guests max
        """
        return {
            RoomType.STANDARD: 2,
            RoomType.DELUXE: 3,
            RoomType.SUITE: 4,
        }[self]
