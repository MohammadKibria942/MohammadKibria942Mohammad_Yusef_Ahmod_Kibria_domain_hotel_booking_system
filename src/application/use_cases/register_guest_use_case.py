from datetime import date
from uuid import uuid4
from src.domain.guest import Guest


# This could be expanded later with a real repository
class RegisterGuestUseCase:
    def __init__(self, save_guest: callable):
        self.save_guest = save_guest  # Function to persist guest

    def execute(self, name: str, email: str, dob: date, phone: str) -> Guest:
        """
        Creates and stores a new guest
        """
        guest = Guest(
            guest_id=str(uuid4()),
            name=name,
            email=email,
            date_of_birth=dob,
            phone=phone,
        )
        self.save_guest(guest)
        return guest
