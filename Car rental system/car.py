import sqlite3
from tabulate import tabulate

DB_FILE = "car_rental.db"

class Car:
    def __init__(self):
        self.car_id = None
        self.make = None
        self.model = None
        self.year = None
        self.mileage = None
        self.price_per_day = None
        self.available_now = None
        self.min_rental_days = None
        self.max_rental_days = None

    def get_input_from_user (self):
        # Validation helper function for input
        def get_input(prompt, validation_func, error_message):
            while True:
                value = input(prompt).strip()
                if validation_func(value):
                    return value
                else:
                    print(error_message)

        # Validation functions
        def is_non_empty(value):
            return bool(value)

        def is_valid_year(value):
            return value.isdigit() and len(value) == 4

        def is_valid_availability(value):
            return value in ["yes", "no"]

        def is_positive_integer(value):
            return value.isdigit() and int(value) > 0 and bool(value)

        # Collect inputs
        # car_id = get_input("Car ID: ", is_positive_integer, "Car ID cannot be blank.")
        self.make = get_input("Make: ", is_non_empty, "Make cannot be blank.")
        self.model = get_input("Model: ", is_non_empty, "Model cannot be blank.")
        self.year = get_input("Year: ", is_valid_year, "Please enter a valid 4-digit year.")
        self.mileage = get_input("Mileage: ", is_positive_integer, "Please enter a number mileage.")
        self.price_per_day = get_input("Price per day: ", is_positive_integer, "Please enter a number")
        self.available_now = get_input("Is the car available now? (yes/no): ", is_valid_availability,
                                  "Invalid input. Please enter 'yes' or 'no'.")

        #converts string to boolean
        self.available_now = 1 if self.available_now == "yes" else 0

        # Handle rental period with validation
        self.min_rental_days = int(
            get_input("Minimum rental period (days): ", is_positive_integer, "Please enter a valid positive number."))
        self.max_rental_days = int(
            get_input("Maximum rental period (days): ", is_positive_integer, "Please enter a valid positive number."))

        # Ensure the minimum rent period is less than or equal to the maximum rent period
        while self.min_rental_days > self.max_rental_days:
            print("Minimum rental period cannot be greater than maximum rental period. Please try again.")
            self.min_rental_days = int(get_input("Minimum rental period (days): ", is_positive_integer,
                                            "Please enter a valid positive number."))
            self.max_rental_days = int(get_input("Maximum rental period (days): ", is_positive_integer,
                                            "Please enter a valid positive number."))

    def add_car(self):
        Car.view_cars()  # Display the current list of cars
        print("\nAdd a new car")

        self.get_input_from_user()

        #using this VALUES ( ?, ?, ?, ?, ?, ?, ?, ?) to avoid  SQL injection vulnerabilities which is
        #a type of attack where an attacker can manipulate SQL queries by inserting or "injecting"
        #malicious SQL code through user inputs. The question marks ? are placeholders for the actual
        #values that will be inserted into the table
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO cars ( make, model, year, mileage, price_per_day, available_now, min_rental_days, "
            "max_rental_days) VALUES ( ?, ?, ?, ?, ?, ?, ?, ?)",
            (self.make, self.model, int(self.year), int(self.mileage), float(self.price_per_day),
             self.available_now, self.min_rental_days, self.max_rental_days)
        )
        conn.commit()
        conn.close()

        print("Car added successfully!\n")


    def update_car(self):
        Car.view_cars()  # Display the current list of cars
        print("\nUpdate car details. Press \"Enter\" to leave blank if no changes to be made")
        car_id = input("Enter the Car ID to update: ").strip()

        if not car_id:
            print("Car ID cannot be empty.\n")
            return

        try:
            with sqlite3.connect(DB_FILE) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT * FROM cars WHERE id = ?", (car_id,))
                car = cursor.fetchone()

            if car:

                # No need for try-except here since strings don’t cause type errors.
                self.make = input("Enter make: ").strip() or car[1]
                self.model = input("Enter model: ").strip() or car[2]

                # Using try-except for numeric inputs to catch conversion errors.
                while True:
                    try:
                        user_input = input("Enter year: ").strip()
                        self.year = int(user_input) if user_input else car[3]
                        break
                    except ValueError:
                        print("Invalid input. Please enter a valid year (e.g., 2022).")

                while True:
                    try:
                        user_input = input("Enter mileage: ").strip()
                        self.mileage = int(user_input) if user_input else car[4]
                        break
                    except ValueError:
                        print("Invalid input. Please enter a valid mileage.")

                while True:
                    try:
                        user_input = input("Enter price per day: ").strip()
                        self.price_per_day = float(user_input) if user_input else car[5]
                        break
                    except ValueError:
                        print("Invalid input. Please enter a valid price (e.g., 29.99).")

                while True:
                    user_input = input("Is the car available now? (yes/no): ").strip().lower()

                    if not user_input:
                        self.available_now = int(car[6])
                        break
                    elif user_input == "yes":
                        self.available_now = 1
                        break
                    elif user_input == "no":
                        self.available_now = 0
                        break
                    else:
                        print("Invalid input. Please enter 'yes' or 'no'.")

                while True:
                    try:
                        user_input = input("Enter minimum rental days: ").strip()
                        self.min_rental_days = int(user_input) if user_input else car[7]
                        break
                    except ValueError:
                        print("Invalid input. Please enter a valid number.")

                while True:
                    try:
                        user_input = input("Enter maximum rental days: ").strip()
                        self.max_rental_days = int(user_input) if user_input else car[8]
                        break
                    except ValueError:
                        print("Invalid input. Please enter a valid number.")


                # Update the car in the database
                cursor.execute(
                    """
                    UPDATE cars SET make = ?, model = ?, year = ?, price_per_day = ?, mileage = ?, available_now = ?,
                    min_rental_days = ?, max_rental_days = ? WHERE id = ?
                    """,
                    (self.make, self.model, self.year, self.price_per_day, self.mileage,
                     self.available_now, self.min_rental_days, self.max_rental_days, car_id)
                )

                conn.commit()
                conn.close()

                print("Car updated successfully!\n")
            else:
                print("Car ID not found.\n")
        except sqlite3.Error as e:
            print(f"An error occurred while accessing the database: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        finally:
            print("Update process completed.\n")


    @staticmethod
    def delete_car():
        """ Ask admin what car to delete based on car id"""
        Car.view_cars()  # view all cars for reference

        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        car_id = input("Enter car ID to delete: ")
        # Get car details of the car ID  in the database
        cursor.execute("SELECT * FROM cars WHERE id = ?", (car_id,))
        car = cursor.fetchone()  # store tuple of car details

        if car:  # If the car is found, `car` will contain a tuple with the car's details
            cursor.execute("DELETE FROM cars WHERE id = ?", (car_id,))
            conn.commit()
            print(f"Car {car_id} deleted successfully!")
        else:
            print("Car ID not found")

        conn.close()

    @staticmethod
    def view_cars():
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        # Fetch all cars, regardless of availability
        cursor.execute("SELECT * FROM cars")
        cars = cursor.fetchall()

        if cars: # If the cars are found, `cars` will contain a tuple with all the car's details
            # Prepare data for tabulation
            headers = ["ID", "Make", "Model", "Year", "Mileage", "Price_Per_Day", "Available Now", "Min_rental_days", "Max_rental_days"]
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

#Use the class name when calling other static methods within the same class.
#It makes it clear that the method is not tied to any object but is purely class-level.