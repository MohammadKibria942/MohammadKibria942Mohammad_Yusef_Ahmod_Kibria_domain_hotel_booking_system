from dataclasses import dataclass, field
from datetime import date
from enum import Enum, auto
from typing import Optional

from .stay_period import StayPeriod
from .booking_reference import BookingReference


#Enum for booking lifecycle status
class BookingStatus(Enum):
    PENDING = auto()
    CONFIRMED = auto()
    CANCELLED = auto()
    CHECKED_IN = auto()
    CHECKED_OUT = auto()


#Enum for payment status
class PaymentStatus(Enum):
    UNPAID = auto()
    PAID = auto()
    FAILED = auto()


#Booking entity is the core of the reservation domain
@dataclass
class Booking:
    reference: BookingReference
    guest_id: str
    room_number: str
    stay_period: StayPeriod
    total_price: int
    status: BookingStatus = field(default=BookingStatus.PENDING)
    payment_status: PaymentStatus = field(default=PaymentStatus.UNPAID)
    created_on: date = field(default_factory=date.today)

    def confirm(self):
        """
        Confirms the booking after successful payment
        """
        if self.payment_status != PaymentStatus.PAID:
            raise ValueError("Cannot confirm booking without payment")
        self.status = BookingStatus.CONFIRMED

    def cancel(self, today: date) -> bool:
        """
        Attempts to cancel the booking
        returns True if cancellation was allowed and processed
        """
        if self.status in [BookingStatus.CHECKED_IN, BookingStatus.CHECKED_OUT]:
            raise ValueError("Cannot cancel a booking after check-in")

        # 48+ hours before check-in: allow cancellation
        delta = self.stay_period.check_in - today
        if delta.days >= 2:
            self.status = BookingStatus.CANCELLED
            return True
        else:
            return False  # Cannot cancel without penalty (not implemented here)

    def check_in(self, today: date):
        """
        Marks booking as checked in
        """
        if self.status != BookingStatus.CONFIRMED:
            raise ValueError("Booking must be confirmed before check-in")
        if today < self.stay_period.check_in:
            raise ValueError("Cannot check in before the check-in date")
        self.status = BookingStatus.CHECKED_IN

    def check_out(self, today: date):
        """
        Marks booking as checked out
        """
        if self.status != BookingStatus.CHECKED_IN:
            raise ValueError("Booking must be checked in before check-out")
        if today < self.stay_period.check_out:
            raise ValueError("Cannot check out before the check-out date")
        self.status = BookingStatus.CHECKED_OUT
