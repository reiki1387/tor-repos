import sqlite3
from datetime import datetime, timedelta
from tabulate import tabulate
from car import Car

#user =User()    #Global. not good practice.

DB_FILE = "car_rental.db"

class Booking:
    def __init__(self, user):
        #instance attribute for access to Singleton attribute user_id
        self.user = user  # Dependency Injection from CarRentalSystem. To access user_id from singleton class

    @staticmethod
    def get_validate_rental_days(car):
        """
        Ask user for duration of car rent
        """
        while True:
            try:
                rental_days = int(input(f"Enter rental duration in days (between {car[7]} and {car[8]} days): "))
                if rental_days < car[7] or rental_days > car[8]:
                    print(f"Rental duration must be between {car[7]} and {car[8]} days.")
                else:
                    return rental_days
            except ValueError:
                print("Please enter a valid number of days.")

    @staticmethod
    def get_validate_start_datetime(now):
        """
        Ask user for start date and time
        """
        start_date_str = input("Enter rental start date (YYYY-MM-DD): ")
        start_time_str = input("Enter rental start time (HH:MM, 24-hour format): ")
        start_datetime = datetime.strptime(f"{start_date_str} {start_time_str}", "%Y-%m-%d %H:%M")
        max_datetime = now + timedelta(days=30)

        if start_datetime < now:
            raise ValueError("Start date or time cannot be in the past. Please try again.")
        if start_datetime > max_datetime:
            raise ValueError(f"Start time cannot be more than 30 days from now ({max_datetime}). Please try again.")
        return start_datetime


    @staticmethod
    def get_booking_details(now, car):
        """ Get start date and rental duration"""
        while True:
            try:
                start_datetime = Booking.get_validate_start_datetime(now)
                rental_days = Booking.get_validate_rental_days(car)
                return start_datetime, rental_days
            except ValueError as e:
                print(e)

    def process_booking(self, conn, cursor, car, car_id, start_datetime, rental_days):
        """
        insert  booking in the database
        """
        end_datetime = start_datetime + timedelta(days=rental_days)
        cost = rental_days * car[5]

        start_datetime_str = start_datetime.strftime("%Y-%m-%d %H:%M")
        end_datetime_str = end_datetime.strftime("%Y-%m-%d %H:%M")

        cursor.execute("UPDATE cars SET available_now = 0 WHERE id = ?", (car_id,))
        cursor.execute(
            '''INSERT INTO bookings (car_id, user_id, start_date, end_date, cost, status)
               VALUES (?, ?, ?, ?, ?, ?)''',
            (car_id, self.user.user_id, start_datetime_str, end_datetime_str, cost, "pending")
        )
        conn.commit()

        print(
            f"Booking confirmed! Start time: {start_datetime_str}, End time: {end_datetime_str}, Total cost: ${cost}.")

    def book_car(self):
        """
        Process booking based on the current date and time
        """
        Car.view_cars()  # Display the current list of cars for reference
        now = datetime.now().replace(microsecond=0)  # Get the current time
        print(f"Today date and time: {now}")
        print("\nBook a Car (must be within 30 days):")

        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        car_id = input("Enter car ID to book: ")
        cursor.execute("SELECT * FROM cars WHERE id = ?", (car_id,))
        car = cursor.fetchone()

        # Check if the car is in the database and status is available
        if car and car[6]:
            start_datetime, rental_days = Booking.get_booking_details(now, car)

            if start_datetime and rental_days:
                self.process_booking(conn, cursor, car, car_id, start_datetime, rental_days)
        else:
            print("Car is not available.")

        conn.close()






    def view_bookings(self):
        """ Display all bookings from the database in a table format"""
        print("\nYour Bookings:")
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM bookings WHERE user_id = ?", (self.user.user_id,))
        bookings = cursor.fetchall()

        #Display if there is booking
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






    def check_pending_status(self,cursor):
        cursor.execute("SELECT * FROM bookings WHERE user_id = ? AND status = 'pending'", (self.user.user_id,))
        have_pending = cursor.fetchall()

        # exit if no booking with pending status
        if not have_pending:
            print("You have no pending bookings to cancel.")
            return False
        else:
            # display pending booking in table format
            headers = ["Booking ID", "Car ID", "Start Date", "End Date", "Cost", "Status"]
            table = [[booking[0], booking[1], booking[3], booking[4], booking[5], booking[6]] for booking in have_pending]
            print(tabulate(table, headers=headers, tablefmt="grid"))
            return True

    def fetch_pending_status (self,cursor, booking_id):

        #find booking id in the database by the user id
        cursor.execute("SELECT * FROM bookings WHERE booking_id = ? AND user_id = ? AND status = 'pending'",
                       (booking_id, self.user.user_id))

        #save details in tuples
        pending = cursor.fetchone()
        return pending

    def cancel_booking(self):
        """  User can cancel his booking  """

        print("\nCancel a Booking")
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        have_pending_booking = self.check_pending_status(cursor)
        if not have_pending_booking:
            return

        booking_id = input("Enter the Booking ID to cancel: ")

        have_pending_status = self.fetch_pending_status(cursor, booking_id)

        if not have_pending_status:
            print(f"No pending booking found with ID {booking_id}. Please try again.")
        else:
            cursor.execute("UPDATE bookings SET status = 'canceled' WHERE booking_id = ?", (booking_id,))
            conn.commit()

            #set the car by car_id to available status after customer cancel booking
            cursor.execute("UPDATE cars SET available_now = 1 WHERE id = ?", (have_pending_status[1],))
            conn.commit()

            print(f"Booking {booking_id} has been successfully canceled.")

        conn.close()





    #
    # @staticmethod
    # def process_admin_action(cursor, choice):
    #     """
    #     Process the options chosen by the admin for the booking
    #     """
    #     booking_id = input("Enter the Booking ID to process: ")
    #     cursor.execute("SELECT * FROM bookings WHERE booking_id = ?", (booking_id,))
    #     selected_booking = cursor.fetchone()
    #
    #     # if booking not found in database
    #     if not selected_booking:
    #         print(f"No booking found with ID {booking_id}. Please try again.")
    #         return
    #
    #     # if the booking number is already approved or rejected
    #     if selected_booking[6] in ["approved", "rejected"] and choice != "3":
    #         print(f"Booking {booking_id} is already {selected_booking[6]} and cannot be modified.")
    #         return
    #
    #     # if booking number is cancelled it cannot be approved
    #     if selected_booking[6] == "canceled" and choice == "1":
    #         print(f"Booking {booking_id} is canceled.You cannot be approved. Either reject or cancel it")
    #         return
    #
    #     # update booking status in the database
    #     if choice == "1":
    #         cursor.execute("UPDATE bookings SET status = 'approved' WHERE booking_id = ?", (booking_id,))
    #         print(f"Booking {booking_id} has been approved.")
    #     elif choice == "2":
    #         cursor.execute("UPDATE bookings SET status = 'rejected' WHERE booking_id = ?", (booking_id,))
    #         cursor.execute("UPDATE cars SET available_now = 1 WHERE id = ?", (selected_booking[1],))
    #         print(f"Booking {booking_id} has been rejected.")
    #     elif choice == "3":
    #         cursor.execute("DELETE FROM bookings WHERE booking_id = ?", (booking_id,))
    #         cursor.execute("UPDATE cars SET available_now = 1 WHERE id = ?", (selected_booking[1],))
    #         print(f"Booking {booking_id} has been deleted.")
    #
    # @staticmethod
    # def manage_bookings():
    #     """
    #     Ask admin what to do with the customer booking
    #     """
    #     print("\nManage Bookings (Admin):")
    #     conn = sqlite3.connect(DB_FILE)
    #     cursor = conn.cursor()
    #
    #     while True:
    #         cursor.execute("SELECT * FROM bookings")
    #         bookings = cursor.fetchall()
    #
    #         if bookings:
    #             headers = ["Booking ID", "Car ID", "User ID", "Start Date", "End Date", "Cost", "Status"]
    #             table = [
    #                 [booking[0], booking[1], booking[2], booking[3], booking[4], booking[5], booking[6]]
    #                 for booking in bookings
    #             ]
    #             print(tabulate(table, headers=headers, tablefmt="grid"))
    #
    #             print("\nOptions:")
    #             print("1. Approve a booking")
    #             print("2. Reject a booking")
    #             print("3. Delete a booking")
    #             print("4. Exit menu")
    #
    #             choice = input("Enter your choice (1-4): ")
    #
    #             if choice == "4":
    #                 print("Exiting the Manage Bookings menu.")
    #                 break
    #
    #             elif choice in ["1", "2", "3"]:
    #                 Booking.process_admin_action(cursor, choice)
    #             else:
    #                 print("Invalid choice! Please select a valid option (1-4).")
    #
    #         else:
    #             print("No bookings to manage.")
    #             break
    #
    #     conn.close()

    @staticmethod
    def process_admin_action(cursor, choice):
        """
        Process the options chosen by the admin for the booking
        """
        booking_id = input("Enter the Booking ID to process: ")
        cursor.execute("SELECT * FROM bookings WHERE booking_id = ?", (booking_id,))
        found_booking = cursor.fetchone()

        # if booking not found in database
        if not found_booking:
            print(f"No booking found with ID {booking_id}. Please try again.")
            return

        # if the booking number is already approved or rejected
        if found_booking[6] in ["approved", "rejected"] and choice != "3":
            print(f"Booking {booking_id} is already {found_booking[6]} and cannot be modified.")
            return

        # if booking number is cancelled it cannot be approved
        if found_booking[6] == "canceled" and choice == "1":
            print(f"Booking {booking_id} is canceled. You cannot approve it. Either reject or delete it.")
            return

        # update booking status in the database
        if choice == "1":
            cursor.execute("UPDATE bookings SET status = 'approved' WHERE booking_id = ?", (booking_id,))
            print(f"Booking {booking_id} has been approved.")
        elif choice == "2":
            cursor.execute("UPDATE bookings SET status = 'rejected' WHERE booking_id = ?", (booking_id,))
            cursor.execute("UPDATE cars SET available_now = 1 WHERE id = ?", (found_booking[1],))
            print(f"Booking {booking_id} has been rejected.")
        elif choice == "3":
            cursor.execute("DELETE FROM bookings WHERE booking_id = ?", (booking_id,))
            cursor.execute("UPDATE cars SET available_now = 1 WHERE id = ?", (found_booking[1],))
            print(f"Booking {booking_id} has been deleted.")

    @staticmethod
    def manage_bookings():
        """
        Ask admin what to do with the customer booking
        """
        print("\nManage Bookings (Admin):")
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        while True:
            print("\nOptions:")
            print("1. Approve a booking")
            print("2. Reject a booking")
            print("3. Delete a booking")
            print("4. View all bookings")
            print("5. Exit menu")

            choice = input("Enter your choice (1-5): ")

            if choice == "5":
                print("Exiting the Manage Bookings menu.")
                break

            elif choice in ["1", "2", "3","4"]:
                # Fetch bookings based on the admin's choice
                if choice == "1":
                    cursor.execute("SELECT * FROM bookings WHERE status = 'pending'")
                elif choice == "2":
                    cursor.execute("SELECT * FROM bookings WHERE status IN ('pending', 'canceled')")
                elif choice == "3":
                    cursor.execute("SELECT * FROM bookings")
                elif choice == "4":
                    cursor.execute("SELECT * FROM bookings")  # View all bookings without modifying

                bookings_found = cursor.fetchall()

                if bookings_found:
                    headers = ["Booking ID", "Car ID", "User ID", "Start Date", "End Date", "Cost", "Status"]
                    table = [
                        [booking[0], booking[1], booking[2], booking[3], booking[4], booking[5], booking[6]]
                        for booking in bookings_found
                    ]
                    print(tabulate(table, headers=headers, tablefmt="grid"))

                    if choice in ["1", "2", "3"]:  # Process action only if it's not just viewing
                        Booking.process_admin_action(cursor, choice)

                else:
                    print("No bookings to manage for the selected action.")

            else:
                print("Invalid choice! Please select a valid option (1-4).")

        conn.close()
