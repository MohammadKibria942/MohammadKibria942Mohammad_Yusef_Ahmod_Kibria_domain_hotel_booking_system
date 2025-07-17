from abc import ABC, abstractmethod
from src.domain.booking import Booking


#Port for handling payments
class PaymentService(ABC):

    @abstractmethod
    def process_payment(self, booking: Booking) -> bool:
        """
        Processes payment for the booking
        returns True if successful, False otherwise
        """
        pass
