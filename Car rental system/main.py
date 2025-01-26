from initialize_database import initialize_database
from car_rental_system import CarRentalSystem

if __name__ == "__main__":
    initialize_database()

    system = CarRentalSystem()
    system.main_menu()




