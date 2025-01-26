from initialize_database import initialize_database
from car_rental_system import CarRentalSystem

if __name__ == "__main__":
    initialize_database()
    # if not check_table_exists():

    #     print("Table 'cars' was not created successfully.")
    # else:
    #     print("Table 'cars' exists.")
    system = CarRentalSystem()
    system.main_menu()

