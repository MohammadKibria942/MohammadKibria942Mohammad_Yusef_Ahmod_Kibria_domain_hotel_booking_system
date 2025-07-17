from abc import ABC, abstractmethod
from typing import Optional, List
from src.domain.booking import Booking
from src.domain.booking_reference import BookingReference


# Port (interface) for the Booking repository
class BookingRepository(ABC):

    @abstractmethod
    def save(self, booking: Booking) -> None:
        """Persist a booking to storage"""
        pass

    @abstractmethod
    def get_by_reference(self, reference: BookingReference) -> Optional[Booking]:
        """Retrieve a booking by its reference number"""
        pass

    @abstractmethod
    def get_all_by_guest(self, guest_id: str) -> List[Booking]:
        """Get all bookings for a guest"""
        pass
