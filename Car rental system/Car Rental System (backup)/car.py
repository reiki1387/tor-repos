import sqlite3
from tabulate import tabulate

DB_FILE = "car_rental.db"

class Car:
    def __init__(self, car_id, make, model, year, mileage, price_per_day, available_now, min_rental_days, max_rental_days):
        self.car_id = car_id
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        self.price_per_day = price_per_day
        self.available_now = available_now
        self.min_rental_days = min_rental_days
        self.max_rental_days = max_rental_days

    @staticmethod
    def add_car():
        Car.view_cars()  # Display the current list of cars
        print("\nAdd a new car")

        # Validation helper function for input
        def get_input(prompt, validation_func, error_message):
            while True:
                value = input(prompt).strip()
                if validation_func(value):
                    return value
                else:
                    print(error_message)

        # Validation functions
        def is_non_empty(value): return bool(value)
        def is_valid_year(value): return value.isdigit() and len(value) == 4
        def is_valid_availability(value): return value in ["yes", "no"]
        def is_positive_integer(value): return value.isdigit() and int(value) > 0 and bool(value)

        # Collect inputs
        # car_id = get_input("Car ID: ", is_positive_integer, "Car ID cannot be blank.")
        make = get_input("Make: ", is_non_empty, "Make cannot be blank.")
        model = get_input("Model: ", is_non_empty, "Model cannot be blank.")
        year = get_input("Year: ", is_valid_year, "Please enter a valid 4-digit year.")
        mileage = get_input("Mileage: ", is_positive_integer, "Please enter a number mileage.")
        price_per_day = get_input("Price per day: ", is_positive_integer,"Please enter a number")
        available_now = get_input("Is the car available now? (yes/no): ", is_valid_availability,
                                  "Invalid input. Please enter 'yes' or 'no'.")
        available_now = 1 if available_now == "yes" else 0

        # Handle rental period with validation
        min_rent_period = int(
            get_input("Minimum rental period (days): ", is_positive_integer, "Please enter a valid positive number."))
        max_rent_period = int(
            get_input("Maximum rental period (days): ", is_positive_integer, "Please enter a valid positive number."))

        # Ensure the minimum rent period is less than or equal to the maximum rent period
        while min_rent_period > max_rent_period:
            print("Minimum rental period cannot be greater than maximum rental period. Please try again.")
            min_rent_period = int(get_input("Minimum rental period (days): ", is_positive_integer,
                                            "Please enter a valid positive number."))
            max_rent_period = int(get_input("Maximum rental period (days): ", is_positive_integer,
                                            "Please enter a valid positive number."))

        # Insert the new car into the database
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO cars ( make, model, year, mileage, price_per_day, available_now, min_rental_days, "
            "max_rental_days) VALUES ( ?, ?, ?, ?, ?, ?, ?, ?)",
            ( make, model, int(year), int(mileage), float(price_per_day), available_now,
             min_rent_period, max_rent_period)
        )
        conn.commit()
        conn.close()

        print("Car added successfully!\n")

    @staticmethod
    def update_car():
        Car.view_cars()  # Display the current list of cars
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
            price_per_day = float(input(f"price_per_day ({car[5]}): ")) or car[5]

            # Validate availability status
            while True:
                available_now = input("Is the car available now? (yes/no): ").strip().lower()
                if available_now in ["yes", "no"]:
                    available_now = 1 if available_now == "yes" else 0
                    break
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")

            min_rent_period = input(f"Minimum rental period ({car[7]}): ") or car[7]
            max_rent_period = input(f"Maximum rental period ({car[8]}): ") or car[8]

            cursor.execute(
                "UPDATE cars SET make = ?, model = ?, year = ?, price_per_day = ?, mileage = ?, available_now = ?,"
                " min_rent_period = ?, max_rent_period = ? WHERE id = ?",
                (make, model, year, mileage, price_per_day, available_now, min_rent_period, max_rent_period, car_id)
            )
            conn.commit()
            print("Car updated successfully!\n")
        else:
            print("Car ID not found.\n")

        conn.close()
    @staticmethod
    def delete_car(car_id):
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        cursor.execute("DELETE FROM cars WHERE id = ?", (car_id,))
        conn.commit()
        print(f"Car {car_id} deleted successfully!")

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
            headers = ["ID", "Make", "Model", "Year", "Mileage", "Price_Per_Day", "Available Now", "Min Rent Period", "Max Rent Period"]
            table = [
                [
                    car[0],  # ID
                    car[1],  # Make
                    car[2],  # Model
                    car[3],  # Year
                    car[4],  # Mileage
                    car[5],
                    "Yes" if car[6] else "No",  # Convert availability to "Yes"/"No"
                    car[7],  # Min Rent Period
                    car[8]  # Max Rent Period
                ]
                for car in cars
            ]
            print("\nAvailable Cars:")
            print(tabulate(table, headers=headers, tablefmt="grid"))
        else:
            print("\nNo cars found in the database.")

        conn.close()
