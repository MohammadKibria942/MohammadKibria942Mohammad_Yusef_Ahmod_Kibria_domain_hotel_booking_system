from dataclasses import dataclass
from datetime import date
from typing import Optional


#Input data for booking creation
@dataclass
class CreateBookingInput:
    guest_id: str
    check_in: date
    check_out: date
    room_type: str
    request_date: date


#Output DTO(Data Transfer Objects) for returning booking info
@dataclass
class BookingDTO:
    reference: str
    room_number: str
    check_in: date
    check_out: date
    total_price: int
    status: str
    payment_status: str
