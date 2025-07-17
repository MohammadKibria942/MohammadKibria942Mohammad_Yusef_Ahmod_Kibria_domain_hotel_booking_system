from datetime import date
from typing import Protocol
from ..guest import Guest
from ..room_type import RoomType
from ..stay_period import StayPeriod
from ..booking_reference import BookingReference
from ..booking import Booking, BookingStatus, PaymentStatus


#Interface (Port) for looking up available rooms
class RoomAvailabilityPort(Protocol):
    def get_available_room(self, room_type: RoomType, period: StayPeriod) -> str:
        ...


#Service to create a valid booking from inputs
class BookingService:
    def __init__(self, room_availability: RoomAvailabilityPort):
        self.room_availability = room_availability

    def create_booking(
        self,
        guest: Guest,
        check_in: date,
        check_out: date,
        room_type: RoomType,
        today: date
    ) -> Booking:
        """
        Creates a new booking with a valid guest, date range, and available room
        """
        if not guest.is_adult(today):
            raise ValueError("Guest must be at least 18 years old")

        stay_period = StayPeriod.create(check_in, check_out, today)
        room_number = self.room_availability.get_available_room(room_type, stay_period)

        if not room_number:
            raise ValueError("No rooms of the requested type are available")

        total_price = room_type.price() * stay_period.number_of_nights()
        reference = BookingReference.generate()

        return Booking(
            reference=reference,
            guest_id=guest.guest_id,
            room_number=room_number,
            stay_period=stay_period,
            total_price=total_price,
            status=BookingStatus.PENDING,
            payment_status=PaymentStatus.UNPAID,
            created_on=today
        )
