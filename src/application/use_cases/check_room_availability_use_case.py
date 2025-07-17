from datetime import date
from typing import List
from src.application.ports.booking_repository import BookingRepository


class CheckRoomAvailabilityUseCase:
    def __init__(self, repository: BookingRepository):
        self.repository = repository

    def execute(self, start_date: date, end_date: date) -> List[str]:
        """
        Returns available room numbers within a given range
        """
        raise NotImplementedError("To be implemented in infrastructure layer")
