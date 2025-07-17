from src.application.dto import CreateBookingInput, BookingDTO
from src.application.ports.booking_repository import BookingRepository
from src.application.ports.payment_service import PaymentService
from src.domain.services.booking_service import BookingService
from src.domain.guest import Guest
from src.domain.room_type import RoomType


# Orchestrates the flow of creating a booking from API input
class CreateBookingUseCase:
    def __init__(
        self,
        booking_service: BookingService,
        booking_repository: BookingRepository,
        payment_service: PaymentService,
        guest_lookup: callable  # Function to get Guest by ID
    ):
        self.booking_service = booking_service
        self.booking_repository = booking_repository
        self.payment_service = payment_service
        self.guest_lookup = guest_lookup

    def execute(self, input_data: CreateBookingInput) -> BookingDTO:
        # Lookup and validate guest
        guest = self.guest_lookup(input_data.guest_id)
        if guest is None:
            raise ValueError("Guest not found")

        # Create the domain booking object using domain service
        room_type = RoomType(input_data.room_type)
        booking = self.booking_service.create_booking(
            guest=guest,
            check_in=input_data.check_in,
            check_out=input_data.check_out,
            room_type=room_type,
            today=input_data.request_date
        )

        # Process payment (mock for now)
        success = self.payment_service.process_payment(booking)
        if not success:
            raise ValueError("Payment failed")

        booking.payment_status = booking.payment_status.PAID
        booking.confirm()

        # Save to repository
        self.booking_repository.save(booking)

        # Return output DTO
        return BookingDTO(
            reference=str(booking.reference),
            room_number=booking.room_number,
            check_in=booking.stay_period.check_in,
            check_out=booking.stay_period.check_out,
            total_price=booking.total_price,
            status=booking.status.name,
            payment_status=booking.payment_status.name,
        )
