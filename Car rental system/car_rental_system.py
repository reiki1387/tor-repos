from user import User
from car import Car
from booking import Booking

class CarRentalSystem:
    # def __init__(self):
    #     self.current_user = None
    _instance = None  # class variable to hold the single instance

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)  # create the instance if it doesn't exist
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'initialized'):  # Ensures the constructor runs only once
            self.initialized = True
            self.current_user = None

    def main_menu(self):
        while True:
            print("\nCar Rental System")
            print("1. Register User")
            print("2. Login")
            print("3. Exit")
            choice = input("Choose an option: ")

            if choice == "1":
                User.register_user()
            elif choice == "2":
                self.current_user = User.login_user()  # assign return value (object)
                if self.current_user:   #check if truthy or falsy
                    if self.current_user.get_role() == "admin":
                        self.admin_menu()
                    elif self.current_user.get_role() == "customer":
                        self.customer_menu()
            elif choice == "3":
                print("Exiting the system. Goodbye!")
                break
            else:
                print("Invalid choice. Try again.")

    def admin_menu(self):
        while True:
            print("\nAdmin Menu")
            print("1. Add Car")
            print("2. Update Car")
            print("3. Delete Car")
            print("4. View Cars")
            print("5. Manage All Bookings")
            print("6. Logout")
            choice = input("Choose an option: ")

            if choice == "1":
                Car.add_car()
            elif choice == "2":
                Car.update_car()
            elif choice == "3":
                car_id = input("Enter car ID to delete: ")
                Car.delete_car(car_id)
            elif choice == "4":
                Car.view_cars()
            elif choice == "5":
                Booking.manage_bookings()
            elif choice == "6":
                break
            else:
                print("Invalid choice. Try again.")

    def customer_menu(self):
        while True:
            print("\nCustomer Menu")
            print("1. View Cars")
            print("2. Book Car")
            print("3. View My Bookings")
            print("4. Cancel a Booking")
            print("5. Logout")
            choice = input("Choose an option: ")

            if choice == "1":
                Car.view_cars()
            elif choice == "2":
                Booking.book_car(self.current_user.user_id)
            elif choice == "3":
                Booking.view_bookings(self.current_user.user_id)
            elif choice == "4":
                Booking.cancel_booking(self.current_user.user_id)
            elif choice == "5":
                break
            else:
                print("Invalid choice. Try again.")

