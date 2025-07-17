from typing import List
from src.application.dto import BookingDTO
from src.application.ports.booking_repository import BookingRepository


class GetGuestBookingsUseCase:
    def __init__(self, booking_repository: BookingRepository):
        self.booking_repository = booking_repository

    def execute(self, guest_id: str) -> List[BookingDTO]:
        """
        Returns all bookings for a given guest
        """
        bookings = self.booking_repository.get_all_by_guest(guest_id)

        return [
            BookingDTO(
                reference=str(b.reference),
                room_number=b.room_number,
                check_in=b.stay_period.check_in,
                check_out=b.stay_period.check_out,
                total_price=b.total_price,
                status=b.status.name,
                payment_status=b.payment_status.name,
            )
            for b in bookings
        ]
