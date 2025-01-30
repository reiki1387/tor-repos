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



    # This method and one of its nested function has a default parameter value "None" to makes the parameter
    # optional when called by the other method that does not provide the required parameter.
    def get_input_from_user(self, defaults=None):
        # Validation helper function for input
        def get_input(prompt, validation_func, error_message, default=None):
            while True: #continue asking for input as long as it displays error message
                value = input(prompt).strip()

                if value:  # If user provides input, validate it
                    if validation_func(value):
                        return value
                    else:
                        print(error_message)
                elif default is not None:  # Allow blank input for updates
                    return default  #returns the value from database, if user leaves input blank
                else:
                    print(error_message) #If user leaves input blank while there is nothing in the database, prompt again

        # Validation functions
        def is_non_empty(value):
            return bool(value)

        def is_valid_year(value):
            return value.isdigit() and len(value) == 4

        def is_valid_availability(value):
            return value in ["yes", "no"]

        def is_positive_integer(value):
            return value.isdigit() and int(value) > 0

        # Use defaults for updates, otherwise force input for new entries
        # the second argument is an application of higher order function/function reference/Firs-class function
        # the 4th argument is an expression that evaluates to a value in the dictionary if it is received as a parameter
        self.make = get_input("Make: ", is_non_empty, "Make cannot be blank.",
                              defaults.get("make") if defaults else None)
        self.model = get_input("Model: ", is_non_empty, "Model cannot be blank.",
                               defaults.get("model") if defaults else None)
        self.year = get_input("Year: ", is_valid_year, "Please enter a valid 4-digit year.",
                              defaults.get("year") if defaults else None)
        self.mileage = get_input("Mileage: ", is_positive_integer, "Please enter a number mileage.",
                                 defaults.get("mileage") if defaults else None)
        self.price_per_day = get_input("Price per day: ", is_positive_integer, "Please enter"
                                             " a number.", defaults.get("price_per_day") if defaults else None)


        # Line 118, check if parameter "defaults" has value and "available now" is equal to yes. I use "==1" to handle
        # the problem wherein when the database has a value of "no", it will be changed to "yes" due to the result of
        # this expression if the user does not input anything.
        #If admin is adding a car,there is nothing in the database, and admin leaves it blank, the availability will
        # defaults to "no"
        availability_default = "yes" if defaults and defaults.get("available_now")==1 else "no"

        self.available_now = get_input("Is the car available now? (yes/no), If new car and no input = no: ",
                                       is_valid_availability, "Invalid input. Please enter 'yes' or 'no'.",
                                        availability_default)

        self.available_now = 1 if self.available_now == "yes" else 0  # Convert to boolean

        self.min_rental_days = int(get_input("Minimum rental period (days): ", is_positive_integer,
                                         "Please enter a valid positive number.",
                                         defaults.get("min_rental_days") if defaults else None))
        self.max_rental_days = int(get_input("Maximum rental period (days): ", is_positive_integer,
                                         "Please enter a valid positive number.",
                                         defaults.get("max_rental_days") if defaults else None))


        # Ensure min rental days is not greater than max rental days
        while self.min_rental_days > self.max_rental_days:
            print("Minimum rental period cannot be greater than maximum rental period. Please try again.")
            self.min_rental_days = int(get_input("Minimum rental period (days): ", is_positive_integer,
                                                 "Please enter a valid positive number.",
                                                 defaults.get("min_rental_days") if defaults else None))
            self.max_rental_days = int(get_input("Maximum rental period (days): ", is_positive_integer,
                                                 "Please enter a valid positive number.",
                                                 defaults.get("max_rental_days") if defaults else None))

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
        Car.view_cars()
        print("\nUpdate car details. Press \"Enter\" to leave blank if no changes are needed")

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
                # Map database row to dictionary for defaults
                defaults = {
                    "make": car[1],
                    "model": car[2],
                    "year": car[3],
                    "mileage": car[4],
                    "price_per_day": car[5],
                    "available_now": car[6],
                    "min_rental_days": car[7],
                    "max_rental_days": car[8]
                }

                self.get_input_from_user(defaults)  # Pass defaults

                with sqlite3.connect(DB_FILE) as conn:
                    cursor = conn.cursor()
                    cursor.execute(
                        """
                        UPDATE cars SET make = ?, model = ?, year = ?, price_per_day = ?, mileage = ?, available_now = ?,
                        min_rental_days = ?, max_rental_days = ? WHERE id = ?
                        """,
                        (self.make, self.model, self.year, self.price_per_day, self.mileage,
                         self.available_now, self.min_rental_days, self.max_rental_days, car_id)
                    )

                print("Car updated successfully!\n")
            else:
                print("Car ID not found.\n")

        except sqlite3.Error as e:   #handles database related errors
            print(f"An error occurred while accessing the database: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")







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