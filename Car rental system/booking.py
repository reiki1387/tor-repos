import sqlite3
from datetime import datetime, timedelta

from car import Car
from tabulate import tabulate

DB_FILE = "car_rental.db"

class Booking:
    def __init__(self, booking_id, car_id, user_id, start_date, end_date, cost, status):
        self.booking_id = booking_id
        self.car_id = car_id
        self.user_id = user_id
        self.start_date = start_date
        self.end_date = end_date
        self.cost = cost
        self.status = status

    @staticmethod
    def book_car(user_id):
        Car.view_cars()  # Display the current list of cars for reference
        now = datetime.now().replace(second=0, microsecond=0)
        print(f"Today date and time: {now}")  # For customer reference
        print("\nBook a Car(must be within 30 days):")

        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        car_id = input("Enter car ID to book: ")
        cursor.execute("SELECT * FROM cars WHERE id = ?", (car_id,))
        car = cursor.fetchone()

        # If car ID is fetched and availability is True
        if car and car[6]:
            while True:  # Loop until valid inputs are provided
                try:
                    # Prompt for start date and time
                    start_date_str = input("Enter rental start date (YYYY-MM-DD): ")
                    start_time_str = input("Enter rental start time (HH:MM, 24-hour format): ")

                    # Combine start date and time into a datetime object
                    start_datetime = datetime.strptime(f"{start_date_str} {start_time_str}", "%Y-%m-%d %H:%M")

                    # Get today's datetime and maximum allowed datetime
                    max_datetime = now + timedelta(days=30)

                    # Validate the start datetime
                    if start_datetime < now:
                        print("Start date or time cannot be in the past. Please try again.")
                        continue
                    if start_datetime > max_datetime:
                        print(f"Start time cannot be more than 30 days from now ({max_datetime}). Please try again.")
                        continue


                    # Ask the customer for the number of rental days
                    while True:
                        try:
                            rental_days = int(
                                input(f"Enter rental duration in days (between {car[7]} and {car[8]} days): "))
                            if rental_days < car[7] or rental_days > car[8]:
                                print(f"Rental duration must be between {car[7]} and {car[8]} days.")
                            else:
                                break
                        except ValueError:
                            print("Please enter a valid number of days.")

                    # Calculate the end time
                    end_datetime = start_datetime + timedelta(days=rental_days)

                    # Convert datetime objects to strings for database storage
                    start_datetime_str = start_datetime.strftime("%Y-%m-%d %H:%M")
                    end_datetime_str = end_datetime.strftime("%Y-%m-%d %H:%M")

                    # Calculate cost based on individual car cost
                    cost = rental_days * car[5]

                    # Update the car's availability in the database
                    cursor.execute("UPDATE cars SET available_now = 0 WHERE id = ?", (car_id,))

                    # Save booking in the database
                    cursor.execute('''
                        INSERT INTO bookings (car_id, user_id, start_date, end_date, cost, status)
                        VALUES (?, ?, ?, ?, ?, ?)
                    ''', (car_id, user_id, start_datetime_str, end_datetime_str, cost, "pending"))
                    conn.commit()

                    print(
                        f"Booking confirmed! Start time: {start_datetime_str}, End time: {end_datetime_str}, Total cost: ${cost}.")
                    break  # Exit the loop

                except ValueError:
                    print("Invalid date, time, or number of days. Please ensure inputs are in the correct format.")
        else:
            print("Car is not available.")

        conn.close()

    # def calculate_late_return_cost(car_id, actual_return_time):
    #     """
    #     Function to calculate the additional cost if the car is returned late.
    #     """
    #     conn = sqlite3.connect(DB_FILE)
    #     cursor = conn.cursor()
    #
    #     # Fetch the booking details
    #     cursor.execute("SELECT end_date, cost, car_id FROM bookings WHERE car_id = ? AND status = 'pending'", (car_id,))
    #     booking = cursor.fetchone()
    #
    #     if booking:
    #         # Retrieve the stored end date and time as a string
    #         end_datetime = datetime.strptime(booking[0], "%Y-%m-%d %H:%M")
    #         daily_rate = booking[5]  # Fetch daily rate from the car details
    #
    #         # Calculate late days (if any)
    #         actual_return_datetime = datetime.strptime(actual_return_time, "%Y-%m-%d %H:%M")
    #         if actual_return_datetime > end_datetime:
    #             late_duration = (actual_return_datetime - end_datetime).total_seconds()
    #             late_days = int(late_duration // 86400)  # Full late days
    #             if late_duration % 86400 != 0:  # Include partial late day
    #                 late_days += 1
    #
    #             additional_cost = late_days * daily_rate
    #             total_cost = booking[1] + additional_cost
    #
    #             print(
    #                 f"Car returned late by {late_days} day(s). Additional cost: ${additional_cost}. Total cost: ${total_cost}.")
    #
    #             # Update booking cost and status
    #             cursor.execute('''
    #                 UPDATE bookings
    #                 SET cost = ?, status = 'completed'
    #                 WHERE car_id = ? AND status = 'pending'
    #             ''', (total_cost, car_id))
    #             conn.commit()
    #         else:
    #             print("Car returned on time. No additional cost.")
    #             cursor.execute('''
    #                 UPDATE bookings
    #                 SET status = 'completed'
    #                 WHERE car_id = ? AND status = 'pending'
    #             ''', (car_id,))
    #             conn.commit()
    #     else:
    #         print("No active booking found for this car.")
    #
    #     conn.close()

    #customer view bookings made
    @staticmethod
    def view_bookings(user_id):
        print("\nYour Bookings:")
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM bookings WHERE user_id = ?", (user_id,))
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

    #customer cancel booking made
    #Instance method- a meth0d being called by an instance of a class
    @staticmethod
    def cancel_booking(user_id):
        """Allows a customer to cancel their booking."""
        print("\nCancel a Booking")
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        # Fetch all the customer's bookings
        cursor.execute("SELECT * FROM bookings WHERE user_id = ? AND status = 'pending'", (user_id,))
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
                       (booking_id, user_id))
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

    #admin manage bookings
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