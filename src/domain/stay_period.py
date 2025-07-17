from dataclasses import dataclass
from datetime import date, timedelta
from typing import Self


@dataclass(frozen=True)
class StayPeriod:
    check_in: date
    check_out: date

    @classmethod
    def create(cls, check_in: date, check_out: date, today: date) -> Self:
        """
        Method to validate and create a StayPeriod instance
        Enforces the following rules:
        Check-in must be at least 24 hours in the future
        Stay cannot be longer than30 nights
        Check-out must be after check-in
        """
        if check_in <= today:
            raise ValueError("Check-in must be at least 24 hours in the future")

        if check_out <= check_in:
            raise ValueError("Check-out must be after check-in")

        max_allowed_checkout = check_in + timedelta(days=30)
        if check_out > max_allowed_checkout:
            raise ValueError("Stay cannot exceed 30 nights")

        return cls(check_in=check_in, check_out=check_out)

    def number_of_nights(self) -> int:
        """
        Returns the number of nights for this stay
        """
        return (self.check_out - self.check_in).days
