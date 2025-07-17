from datetime import date
from src.application.ports.booking_repository import BookingRepository
from src.domain.booking_reference import BookingReference


class CheckInUseCase:
    def __init__(self, booking_repository: BookingRepository):
        self.booking_repository = booking_repository

    def execute(self, reference: str, today: date) -> None:
        """
        Marks booking as checked in if allowed
        """
        ref = BookingReference(reference)
        booking = self.booking_repository.get_by_reference(ref)

        if not booking:
            raise ValueError("Booking not found")

        booking.check_in(today)
