from src.application.dto import BookingDTO
from src.application.ports.booking_repository import BookingRepository
from src.domain.booking_reference import BookingReference


class GetBookingDetailsUseCase:
    def __init__(self, booking_repository: BookingRepository):
        self.booking_repository = booking_repository

    def execute(self, reference: str) -> BookingDTO:
        """
        Returns booking info by reference
        """
        ref = BookingReference(reference)
        booking = self.booking_repository.get_by_reference(ref)

        if not booking:
            raise ValueError("Booking not found")

        return BookingDTO(
            reference=str(booking.reference),
            room_number=booking.room_number,
            check_in=booking.stay_period.check_in,
            check_out=booking.stay_period.check_out,
            total_price=booking.total_price,
            status=booking.status.name,
            payment_status=booking.payment_status.name,
        )
