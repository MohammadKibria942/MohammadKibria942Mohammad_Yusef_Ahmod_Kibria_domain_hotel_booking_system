from dataclasses import dataclass
from datetime import date


#Guest is an entity representing a person who books a room at the hotel.
@dataclass
class Guest:
    guest_id: str      #Unique identifier for the guest
    name: str
    email: str
    date_of_birth: date
    phone: str

    def is_adult(self, today: date) -> bool:
        """
        Validates that the guest is at least 18 years old
        """
        age = today.year - self.date_of_birth.year
        if (today.month, today.day) < (self.date_of_birth.month, self.date_of_birth.day):
            age -= 1
        return age >= 18
