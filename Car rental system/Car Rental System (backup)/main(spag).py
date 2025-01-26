import sqlite3
from tabulate import tabulate
from datetime import datetime, timedelta

DB_FILE = "car_rental.db"

def initialize_database():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    # Create the cars table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cars (
            id TEXT PRIMARY KEY,
            make TEXT NOT NULL,
            model TEXT NOT NULL,
            year INTEGER NOT NULL,
            mileage INTEGER NOT NULL,
            available_now BOOLEAN NOT NULL,
            min_rent_period INTEGER NOT NULL,
            max_rent_period INTEGER NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users(
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            role TEXT NOT NULL
        )
    ''')


    # Create the bookings table if it doesn't exist
    cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS bookings (
            booking_id INTEGER PRIMARY KEY AUTOINCREMENT,
            car_id TEXT NOT NULL,
            user_id TEXT NOT NULL,
            start_date TEXT NOT NULL,
            end_date TEXT NOT NULL,
            cost INTEGER NOT NULL,
            status TEXT NOT NULL,  -- 'pending', 'approved', 'rejected', 'canceled'
            FOREIGN KEY (car_id) REFERENCES cars(id),
            FOREIGN KEY (user_id) REFERENCES users(username)
        )
    ''')

    # Check if the table is empty
    cursor.execute("SELECT COUNT(*) FROM cars")
    if cursor.fetchone()[0] == 0:
        # Insert initial car data
        initial_cars = [
            ("C001", "Toyota", "Corolla", 2020, 15000, True, 2, 30),
            ("C002", "Honda", "Civic", 2019, 20000, True, 3, 25),
            ("C003", "Ford", "Focus", 2021, 10000, True, 1, 20),
            ("C004", "Chevrolet", "Cruze", 2018, 30000, True, 5, 40),
            ("C005", "Nissan", "Sentra", 2020, 18000, True, 2, 30),
        ]

        cursor.executemany('''
            INSERT INTO cars (id, make, model, year, mileage, available_now, min_rent_period, max_rent_period)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', initial_cars)

        print("Initialized the database with default car data.")




class Admin:
    def __init__(self, username, role):
        self.username = username
        self.role = role

    def get_role(self):
        return self.role

class Customer:
    def __init__(self, username, role):
        self.username = username
        self.role = role

    def get_role(self):
        return self.role



# Car Class
class Car:
    def __init__(self, car_id, make, model, year, mileage, available_now, min_rent_period, max_rent_period):
        self.id = car_id
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        self.available_now = available_now
        self.min_rent_period = min_rent_period
        self.max_rent_period = max_rent_period


class Booking:
    def __init__(self, car_id, start_date, end_date, cost):
        self.car_id = car_id
        self.start_date = start_date
        self.end_date = end_date
        self.cost = cost

class CarRentalSystem:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.current_user = None  # Track the current logged-in user
            self.initialized = True


    @staticmethod
    def register_user():
        print("\nRegister a New User")
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        username = input("Enter a username: ").strip()
        password = input("Enter a password: ").strip()
        role = input("Enter role (admin/customer): ").strip().lower()

        #Validate the role input
        while role not in ["admin", "customer"]:
            print("Invalid role. Please enter 'admin' or 'customer'.")
            role = input("Enter role (admin/customer): ").strip().lower()

        # Check if the username already exists
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        if cursor.fetchone():
            print("Username already exists. Please choose a different username.")
        else:
            # Insert the new user into the database
            cursor.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", (username, password, role))
            conn.commit()
            print(f"User '{username}' registered successfully as {role}.")

        conn.close()

    def login_user(self):
        """
        Authenticates the user and returns a user object (Admin or Customer) upon successful login.
        """
        print("\nLogin to the system")
        username = input("Enter username: ").strip()
        password = input("Enter password: ").strip()

        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        # Fetch specific user record from the database
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        user_record = cursor.fetchone()  #list of tuples data type
        print(user_record)



        if not username or not password:
            print("Username and password cannot be empty. Please try again.")
            return None

        if not user_record:
            print("User not found. Please register first.")
            conn.close()
            return None

        # Extract data from tuples of database record and assign to variables
        db_username, db_password, db_role = user_record


        # Validate password
        if password != db_password:  # Replace this with hash comparison if passwords are hashed
            print("Incorrect password. Please try again.")
            conn.close()
            return None

        self.current_user = db_username

        print(f"Welcome back, {db_username}!")
        conn.close()

        # Instantiate user object based on role
        if db_role == "admin":
            return Admin(username=db_username, role=db_role)
        elif db_role == "customer":
            return Customer(username=db_username, role=db_role)
        else:
            print("Invalid role detected. Contact the administrator.")
            return None

    def add_car(self):
        self.view_cars()  # Display the current list of cars
        print("\nAdd a new car")
        car_id = input("Car ID: ")
        make = input("Make: ")
        model = input("Model: ")
        year = input("Year: ")
        mileage = input("Mileage: ")

        while True:
            available_now = input("Is the car available now? (yes/no): ").strip().lower()
            if available_now in ["yes", "no"]:
                available_now = 1 if available_now == "yes" else 0
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
        min_rent_period = int(input("Minimum rental period (days): "))
        max_rent_period = int(input("Maximum rental period (days): "))

        # Insert new car into the database
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO cars (id, make, model, year, mileage, available_now, min_rent_period, max_rent_period) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            (car_id, make, model, year, mileage, int(available_now), min_rent_period, max_rent_period)
        )
        conn.commit()
        conn.close()

        print("Car added successfully!\n")

    def update_car(self):
        self.view_cars()  # Display the current list of cars
        print("\nUpdate car details")
        car_id = input("Enter the Car ID to update: ").title()

        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM cars WHERE id = ?", (car_id,))
        car = cursor.fetchone()

        if car:
            print("Leave fields blank if no update is needed.")
            make = input(f"Make ({car[1]}): ") or car[1]
            model = input(f"Model ({car[2]}): ") or car[2]
            year = input(f"Year ({car[3]}): ") or car[3]
            mileage = input(f"Mileage ({car[4]}): ") or car[4]

            # Validate availability status
            while True:
                available_now = input("Is the car available now? (yes/no): ").strip().lower()
                if available_now in ["yes", "no"]:
                    available_now = 1 if available_now == "yes" else 0
                    break
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")

            min_rent_period = input(f"Minimum rental period ({car[6]}): ") or car[6]
            max_rent_period = input(f"Maximum rental period ({car[7]}): ") or car[7]

            cursor.execute(
                "UPDATE cars SET make = ?, model = ?, year = ?, mileage = ?, available_now = ?,"
                " min_rent_period = ?, max_rent_period = ? WHERE id = ?",
                (make, model, year, mileage, available_now, min_rent_period, max_rent_period, car_id)
            )
            conn.commit()
            print("Car updated successfully!\n")
        else:
            print("Car ID not found.\n")

        conn.close()

    def delete_car(self):
        self.view_cars()  # Display the current list of cars
        print("\nDelete a car")
        car_id = input("Enter the Car ID to delete: ")

        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM cars WHERE id = ?", (car_id,))
        car = cursor.fetchone()

        if car:
            cursor.execute("DELETE FROM cars WHERE id = ?", (car_id,))
            conn.commit()
            print("Car deleted successfully!\n")
        else:
            print("Car ID not found.\n")

        conn.close()

    @staticmethod
    def view_cars():
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        # Fetch all cars, regardless of availability
        cursor.execute("SELECT * FROM cars")
        cars = cursor.fetchall()

        if cars:
            # Prepare data for tabulation
            headers = ["ID", "Make", "Model", "Year", "Mileage", "Available Now", "Min Rent Period", "Max Rent Period"]
            table = [
                [
                    car[0],  # ID
                    car[1],  # Make
                    car[2],  # Model
                    car[3],  # Year
                    car[4],  # Mileage
                    "Yes" if car[5] else "No",  # Convert availability to "Yes"/"No"
                    car[6],  # Min Rent Period
                    car[7]  # Max Rent Period
                ]
                for car in cars
            ]
            print("\nAvailable Cars:")
            print(tabulate(table, headers=headers, tablefmt="grid"))
        else:
            print("\nNo cars found in the database.")

        conn.close()

    # Function to validate time input format
    @staticmethod
    def get_valid_time_input():
        while True:
            time_input = input("Enter rental start time in 24H time format (HH:MM)")
            try:
                # Try to parse the time to ensure it's in the correct format
                datetime.strptime(time_input, "%H:%M")
                return time_input  # Valid time format
            except ValueError:
                print("Invalid time format. Please enter the time in 24H and HH:MM:SS format.")

    @staticmethod
    def get_valid_date_input():
        """Ensures that the user enters a valid date in YYYY-MM-DD format."""
        while True:
            try:
                start_date_str = input("Enter rental start date (YYYY-MM-DD): ")

                # Attempt to parse the date string
                datetime.strptime(start_date_str, "%Y-%m-%d")
                return start_date_str  # Valid date format
            except ValueError:
                print("Invalid date format. Please enter the date in YYYY-MM-DD format.")



    def book_car(self):
        self.view_cars()  # Display the current list of cars for reference
        print("\nBook a car")
        car_id = input("Enter the Car ID to book: ").title()

        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        # Check if the car exists and is available
        cursor.execute("SELECT * FROM cars WHERE id = ?", (car_id,))
        car = cursor.fetchone()

        if car:
            if not car[5]:  # Check availability (car[5] is the `available_now` field)
                print("The car is not available for booking.\n")
            else:
                # Get today's date
                today = datetime.today()  # .date()
                current_datetime_no_seconds =today.replace(second=0 ,microsecond=0)
                while True:
                    print(f"\nToday is {current_datetime_no_seconds}\n")
                    # Get a valid rental start DATE from the user
                    start_date = self.get_valid_date_input()
                    # Check if the start date is in the future but not more than 10 days ahead

                    # Get a valid rental start TIME from the user
                    start_time = self.get_valid_time_input()

                    # Combine the date and time into a single string (date + time)
                    full_datetime_str = f"{start_date} {start_time}"

                    # Convert the entered combined start date to a datetime object
                    start_datetime = datetime.strptime(full_datetime_str, "%Y-%m-%d %H:%M")

                    if start_datetime < current_datetime_no_seconds:
                        print("Start date cannot be in the past. Please enter a valid start date.")
                    elif start_datetime > current_datetime_no_seconds + timedelta(days=10,seconds=0, microseconds=0 ):
                        print("Start date must be within the next 10 days. Please enter a valid start date.")
                    else:
                        break  # Valid start date entered


                # Ask the customer for the number of rental days
                while True:
                    try:
                        rental_days = int(
                            input(f"Enter rental duration in days (between {car[6]} and {car[7]} days): "))
                        if rental_days < car[6] or rental_days > car[7]:
                            print(f"Rental duration must be between {car[6]} and {car[7]} days.")
                        else:
                            break
                    except ValueError:
                        print("Please enter a valid number of days.")

                # Calculate the end date
                end_date = start_datetime + timedelta(days=rental_days)

                # Calculate the cost (e.g., $50 per day)
                cost = rental_days * 50  # Example daily rental fee

                print( f"Booking confirmed! Total cost: ${cost}. Start Date: {start_date} | End Date: "
                       f"{end_date.date()}.\n")

                # Update the car's availability in the database
                cursor.execute("UPDATE cars SET available_now = 0 WHERE id = ?", (car_id,))

                # .isoformat() convert datetime to string to fix "DeprecationWarning" caused by built-in sqlite3
                # .replace() replaces the "T" with space in 'YYYY-MM-DDTHH:MM:SS'
                end_date_iso = end_date.isoformat().replace("T", " ")

                # Insert the booking into the bookings table with status 'pending'
                cursor.execute(''' 
                        INSERT INTO bookings (car_id, user_id, start_date, end_date, cost, status)
                        VALUES (?, ?, ?, ?, ?, ?)
                    ''', (car_id, self.current_user, start_date, end_date_iso, cost, 'pending'))

                conn.commit()
                conn.close()

        else:
            print("Car not found.\n")

        conn.close()

    def cancel_booking(self):
        """Allows a customer to cancel their booking."""
        print("\nCancel a Booking")
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        # Fetch all the customer's bookings
        cursor.execute("SELECT * FROM bookings WHERE user_id = ? AND status = 'pending'", (self.current_user,))
        bookings = cursor.fetchall()

        if not bookings:
            print("You have no pending bookings to cancel.")
            conn.close()
            return

        # Display the customer's bookings
        headers = ["Booking ID", "Car ID", "Start Date", "End Date", "Cost", "Status"]
        table = [[booking[0], booking[1], booking[3], booking[4], booking[5], booking[6]] for booking in bookings]
        print(tabulate(table, headers=headers, tablefmt="grid"))

        # Prompt the user to select a booking to cancel
        booking_id = input("Enter the Booking ID to cancel: ")

        # Check if the selected booking exists and is pending
        cursor.execute("SELECT * FROM bookings WHERE booking_id = ? AND user_id = ? AND status = 'pending'",
                       (booking_id, self.current_user))
        booking = cursor.fetchone()

        if not booking:
            print(f"No pending booking found with ID {booking_id}. Please try again.")
        else:
            # Update the booking status to 'canceled'
            cursor.execute("UPDATE bookings SET status = 'canceled' WHERE booking_id = ?", (booking_id,))
            conn.commit()
            # Restore car availability if booking is rejected
            cursor.execute("UPDATE cars SET available_now = 1 WHERE id = ?", (booking[1],))
            conn.commit()
            print(f"Booking {booking_id} has been successfully canceled.")

        conn.close()

    def view_bookings(self):
        print("\nYour Bookings:")
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM bookings WHERE user_id = ?", (self.current_user,))
        bookings = cursor.fetchall()

        if bookings:
            headers = ["Booking ID", "Car ID", "Start Date", "End Date", "Cost", "Status"]
            table = [
                [booking[0], booking[1], booking[3], booking[4], booking[5], booking[6]]
                for booking in bookings
            ]
            print(tabulate(table, headers=headers, tablefmt="grid"))
        else:
            print("You have no bookings.")

        conn.close()

    @staticmethod
    def manage_bookings():
        print("\nManage Bookings (Admin):")
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        while True:
            cursor.execute("SELECT * FROM bookings")
            bookings = cursor.fetchall()

            if bookings:
                # Display all bookings in a table format
                headers = ["Booking ID", "Car ID", "User ID", "Start Date", "End Date", "Cost", "Status"]
                table = [
                    [booking[0], booking[1], booking[2], booking[3], booking[4], booking[5], booking[6]]
                    for booking in bookings
                ]
                print(tabulate(table, headers=headers, tablefmt="grid"))

                # Admin action menu
                print("\nOptions:")
                print("1. Approve a booking")
                print("2. Reject a booking")
                print("3. Delete a booking")
                print("4. Exit menu")

                choice = input("Enter your choice (1-4): ")

                if choice == "4":  # Exit option
                    print("Exiting the Manage Bookings menu.")
                    break

                elif choice in ["1", "2", "3"]:  # Actions: Approve, Reject, Delete
                    booking_id = input("Enter the Booking ID to process: ")
                    cursor.execute("SELECT * FROM bookings WHERE booking_id = ?", (booking_id,))
                    selected_booking = cursor.fetchone()

                    if not selected_booking:
                        print(f"No booking found with ID {booking_id}. Please try again.")
                        continue

                    # Check if booking is already approved or rejected
                    if selected_booking[6] in ["approved", "rejected"]:
                        if choice != "3":  # choice delete is not included
                            print(f"Booking {booking_id} is already {selected_booking[6]} and cannot be modified.")
                            continue

                    # Restrict actions on canceled bookings
                    if selected_booking[6] == "canceled":
                        if choice == "1":  # Attempt to approve
                            print(
                                f"Booking {booking_id} is canceled and cannot be approved. Only rejection or deletion is allowed.")
                            continue

                    if choice == "1":  # Approve
                        status = "approved"
                        cursor.execute("UPDATE bookings SET status = ? WHERE booking_id = ?", (status, booking_id))
                        conn.commit()
                        print(f"Booking {booking_id} has been approved.")

                    elif choice == "2":  # Reject
                        status = "rejected"
                        cursor.execute("UPDATE bookings SET status = ? WHERE booking_id = ?", (status, booking_id))

                        # Restore car availability if booking is rejected
                        cursor.execute("UPDATE cars SET available_now = 1 WHERE id = ?", (selected_booking[1],))
                        conn.commit()
                        print(f"Booking {booking_id} has been rejected.")

                    elif choice == "3":  # Delete
                        cursor.execute("DELETE FROM bookings WHERE booking_id = ?", (booking_id,))

                        # Restore car availability if booking is deleted
                        cursor.execute("UPDATE cars SET available_now = 1 WHERE id = ?", (selected_booking[1],))
                        conn.commit()
                        print(f"Booking {booking_id} has been deleted from the admin database.")

                else:
                    print("Invalid choice! Please select a valid option (1-4).")

            else:
                print("No bookings to manage.")
                break

        conn.close()

    def main_menu(self):
        while True:
            print("\nCar Rental System")
            print("1. Register User")
            print("2. Login")
            print("3. Exit")

            choice = input("Choose an option: ")

            if choice == "1":
                self.register_user()
            elif choice == "2":
                user = self.login_user()
                if user:
                    if user.get_role() == "admin":
                        self.admin_menu()
                    elif user.get_role() == "customer":
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
            print("4. Manage Bookings")  # Added option to manage all bookings
            print("5. Logout")

            admin_choice = input("Choose an option: ")

            if admin_choice == "1":
                self.add_car()
            elif admin_choice == "2":
                self.update_car()
            elif admin_choice == "3":
                self.delete_car()
            elif admin_choice == "4":
                self.manage_bookings()  # Function to approve or reject bookings
            elif admin_choice == "5":
                break
            else:
                print("Invalid choice. Try again.")

    def customer_menu(self):
        while True:
            print("\nCustomer Menu")
            print("1. View Cars")
            print("2. Book Car")
            print("3. View My Bookings")  # Added this option to view their own bookings
            print("4. Cancel Booking")  # Added this option
            print("5. Logout")

            customer_choice = input("Choose an option: ")

            if customer_choice == "1":
                self.view_cars()
            elif customer_choice == "2":
                self.book_car()
            elif customer_choice == "3":  # Customer views their own bookings here
                self.view_bookings()
            elif customer_choice == "4":
                self.cancel_booking()  # New method for cancellation
            elif customer_choice == "5":
                break
            else:
                print("Invalid choice. Try again.")


if __name__ == "__main__":
    initialize_database()
    # if not check_table_exists():

    #     print("Table 'cars' was not created successfully.")
    # else:
    #     print("Table 'cars' exists.")
    system = CarRentalSystem()
    system.main_menu()

