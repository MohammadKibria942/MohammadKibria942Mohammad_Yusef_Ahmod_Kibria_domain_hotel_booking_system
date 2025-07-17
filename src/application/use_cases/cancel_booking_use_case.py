from datetime import date
from src.application.ports.booking_repository import BookingRepository
from src.domain.booking_reference import BookingReference


class CancelBookingUseCase:
    def __init__(self, booking_repository: BookingRepository):
        self.booking_repository = booking_repository

    def execute(self, reference: str, request_date: date) -> bool:
        """
        Attempts to cancel a booking. Returns True if successful
        """
        ref = BookingReference(reference)
        booking = self.booking_repository.get_by_reference(ref)

        if not booking:
            raise ValueError("Booking not found")

        return booking.cancel(request_date)
