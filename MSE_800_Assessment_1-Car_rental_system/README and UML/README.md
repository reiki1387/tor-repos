# Car Rental System

Github repository-     https://github.com/reiki1387/tor-repos.git
Car Rental prject direct link-    https://github.com/reiki1387/tor-repos/tree/master/Car%20rental%20system

## Overview
The **Car Rental System** is a console-based application designed for managing car rentals. It allows users to register, log in, and book cars, while administrators can manage cars and bookings. The system is built using Python and SQLite for database management.

## Features
- **User Management:** Register and log in as an admin or customer.
- **Car Management:** Admins can add, update, view, and delete cars.
- **Booking Management:** Customers can book, view, and cancel bookings.
- **Admin Controls:** Approve, reject, delete or view all bookings.

## Technologies Used
- **Programming Language:** Python
- **Database:** SQLite
- **Libraries:**
  - `sqlite3` (database management)
  - `tabulate` (formatted table display)
  - `datetime` (handling dates and times)

-------------------------------------------------------------------------------------------------------

## Setup Instructions
### Prerequisites
Ensure you have the following installed:
- Python 3.13
- Required dependencies (install using `pip`):
  pip install tabulate
  

### Database Initialization
The booking, user and car databases are automatically initialized upon activation of .exe file
The database has been initialize to 5 default car details

### Running the Application
1. The .exe file is located at the "dist" folder. Just click to run it
2.Another way is to copy all the files in the folder, inlcuding the environment  and run the main.py in your IDE


--------------------------------------------------------------------------------------------------
## User Roles
- **Admin:** Manages cars and bookings.
- **Customer:** Books and manages their rentals.


## Usage Guide
### 1. Register or Log In
Upon running the system, users can:
- Register as a **customer** or **admin**. Repetition of username is not allowed. User can only choose
- role between "customer" and "admin"
- username, password and role will be saved in the database

### 2. Admin Functions
Once logged in as an **admin**, the following options are available:
- **Add a Car:** Enter car details to add to the database. New car details are mandatory to fill. Admin can leave
		blank (press"Enter") on the availability of the car and it will default to "no"
- **Update a Car:** Modify existing car details. Admin can chose to press "Enter" to leave blank on the details 
		that don't need any change
- **Delete a Car:** Remove a car from the database by inputting car ID
- **View Cars:** Display all available cars.
- **Manage Bookings:** Approve, reject, delete or view all bookings. Admin can only approve booking with "pending" status.
			"Cancelled" booking by customer can be rejected or deleted but cannot be approved. Any "pending" booking
			that has been "rejected" or "deleted", the car will be available again for booking

### 3. Customer Functions
After logging in as a **customer**, users can:
- **View Available Cars:** List all cars both available and not.
- **Book a Car:** Choose available car and ask to input rental duration. The date and time will be diplayed. Customer
		should not input past date and time and their booking start peroid should be not above 30 days. Correct format of date
		and time should be observed. The time  format uses 24H format and should be in a HH:MM format
			. 
- **View My Bookings:** Customer can see past and current booking.
- **Cancel a Booking:** Only pending booking can be cancelled.

------------------------------------------------------------------------------------------------

## Project Structure
```
📂 Car Rental System
│-- 📄 main.py                # Entry point of the system
│-- 📄 car_rental_system.py   # Main system logic
│-- 📄 user.py                # User authentication and management
│-- 📄 car.py                 # Car management operations
│-- 📄 booking.py             # Booking management operations
│-- 📄 initialize_database.py # Database setup
│-- 📂 data                   # SQLite database (car_rental.db)
```

------------------------------------------------------------------------------------------------------------

## Code Summary

The Car Rental System is designed to facilitate user registration, car bookings, and rental management. The system consists of multiple Python modules, each handling a specific functionality. Below is a breakdown of the key components:

1. main.py
This is the entry point of the application. It initializes the database and launches the car rental system's main menu.

Calls initialize_database() to set up tables and insert initial data if necessary.
Creates an instance of CarRentalSystem and starts the user interaction via main_menu().
2. initialize_database.py
This module is responsible for setting up and maintaining the SQLite database.

Creates three tables:
users (Stores user credentials and roles)
cars (Stores car details like make, model, year, mileage, and rental price)
bookings (Tracks user reservations and booking status)
Pre-populates the cars table with some sample vehicles if the database is empty.
3. user.py
This module defines the User class and handles user authentication.

Key Functionalities:
User class: Represents a user with attributes (user_id, username, password, role).
register_user()
Allows new users to sign up as either admin or customer.
Checks if the username already exists before adding a new user to the database.
login_user()
Authenticates users based on their username and password.
Returns a User object upon successful login.
4. car.py
This module defines the Car class, representing a vehicle available for rent.

Key Functionalities:
Attributes:
car_id, make, model, year, mileage, price_per_day, available_now, min_rental_days, max_rental_days
Methods:
Fetch car details from the database.
Check car availability for booking.
5. booking.py
Handles the reservation process, allowing users to book cars.

Key Functionalities:
Booking class:
Attributes: booking_id, car_id, user_id, start_date, end_date, cost, status
Methods:
Book a car for a specific period.
Calculate the total rental cost based on the number of days and price per day.
Update booking status (pending, approved, rejected, cancelled).
6. car_rental_system.py
This is the core module that integrates all other components and provides the main functionalities.

Key Functionalities:
User Management
Allows users to register and log in.
Differentiates between admins and customers.
Car Management
Displays available cars.
Allows customers to select and book cars.
Booking System
Enables users to place bookings.
Provides admins with the ability to approve or reject bookings.


---------------------------------------------------------------------------------------------------------

## Future Improvements
- Implement a **GUI** for a better user experience.
- Add **payment integration** for online booking.
- Improve **error handling** and input validation.

--------------------------------------------------------------------------------------------------

## License
This project is open-source and free to use.

