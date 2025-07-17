import random
import string

#BookingReference is a value object representing a 10 character booking code.
class BookingReference:
    def __init__(self, value: str):
        if len(value) != 10 or not value.isalnum():
            raise ValueError("Booking reference must be a 10 character code")
        self._value = value

    @property
    def value(self) -> str:
        """
        Returns the string representation of the booking reference
        """
        return self._value

    @staticmethod
    def generate() -> 'BookingReference':
        """
        Generates a new random 10 character booking reference
        """
        characters = string.ascii_uppercase + string.digits
        code = ''.join(random.choices(characters, k=10))
        return BookingReference(code)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, BookingReference):
            return False
        return self._value == other._value

    def __str__(self) -> str:
        return self._value
