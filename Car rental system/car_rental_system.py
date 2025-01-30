from user import User
from car import Car
from booking import Booking
#user = User()  #Global. not good practice

class CarRentalSystem:
    #user = User()   #class level attribute, do not allow dependency injection. For utility class only.
    def __init__(self):
        #instance attribute, for encapsulation and to be able to do dependency injection to Bookings
        self.user = User()  # Singleton instance, to get user_role from singleton class
        self.bookings = Booking(self.user)  # Dependency Injection. Inject into Bookings
        self.car = Car()

    def main_menu(self):

        while True:
            print("\nCar Rental System")
            print("1. Register admin")
            print("2. Login")
            print("3. Exit")
            choice = input("Choose an option: ")
            if choice == "1":
                # self.user.register_user()
                self.user.register_admin()
            elif choice == "2":
                log_in_success =self.user.login_user()
                if log_in_success:
                    if self.user.role == "admin":
                        self.admin_menu()
                    elif self.user.role == "customer":
                        self.customer_menu()
            elif choice == "3":
                print("Exiting the system. Goodbye!")
                break
            else:
                print("Invalid choice. Try again.")


    def admin_menu(self):
        while True:
            print("\nAdmin Menu")
            print("1. Register user")
            print("2. Add Car")
            print("3. Update Car")
            print("4. Delete Car")
            print("5. View Cars")
            print("6. Manage All Bookings")
            print("7. Logout")
            choice = input("Choose an option: ")

            if choice == "1":
                self.user.register_user()
            elif choice == "2":
                self.car.add_car()
            elif choice == "3":
                self.car.update_car()
            elif choice == "4":
                Car.delete_car()  #static method. Using class name
            elif choice == "5":
                Car.view_cars()   #static method. Using class name
            elif choice == "6":
                self.bookings.manage_bookings()
            elif choice == "7":
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
                Car.view_cars()    #static method. Using class name
            elif choice == "2":
                self.bookings.book_car()
            elif choice == "3":
                self.bookings.view_bookings()
            elif choice == "4":
                self.bookings.cancel_booking()
            elif choice == "5":
                break
            else:
                print("Invalid choice. Try again.")

