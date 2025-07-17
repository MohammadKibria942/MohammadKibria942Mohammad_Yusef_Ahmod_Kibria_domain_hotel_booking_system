from datetime import date
from src.application.ports.booking_repository import BookingRepository
from src.domain.booking_reference import BookingReference


class CheckOutUseCase:
    def __init__(self, booking_repository: BookingRepository):
        self.booking_repository = booking_repository

    def execute(self, reference: str, today: date) -> None:
        """
        Marks booking as checked out
        """
        ref = BookingReference(reference)
        booking = self.booking_repository.get_by_reference(ref)

        if not booking:
            raise ValueError("Booking not found")

        booking.check_out(today)
