from abc import ABC, abstractmethod
from typing import List
from datetime import date

from ..room_type import RoomType
from ..stay_period import StayPeriod


#Interface to check room availability
class AvailabilityService(ABC):
    @abstractmethod
    def get_available_room(self, room_type: RoomType, period: StayPeriod) -> str:
        """
        Returns a single available room number of the requested type and date range
        raises an exception or returns None if no room is found
        """
        pass

    @abstractmethod
    def list_available_rooms(self, start_date: date, end_date: date) -> List[str]:
        """
        Returns a list of all room numbers available between a given time frame
        """
        pass
