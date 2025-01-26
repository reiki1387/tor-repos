import sqlite3

DB_FILE = "car_rental.db"

def initialize_database():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    # Create users table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL,
            password TEXT NOT NULL,
            role TEXT NOT NULL
        )
    ''')

    # Create cars table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cars (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            make TEXT NOT NULL,
            model TEXT NOT NULL,
            year INTEGER NOT NULL,
            mileage INTEGER NOT NULL,
            price_per_day REAL NOT NULL,
            available_now BOOLEAN NOT NULL,
            min_rental_days INTEGER NOT NULL,
            max_rental_days INTEGER NOT NULL
        )
    ''')

    # Create bookings table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS bookings (
            booking_id INTEGER PRIMARY KEY AUTOINCREMENT,
            car_id INTEGER NOT NULL,
            user_id INTEGER NOT NULL,
            start_date TEXT NOT NULL,
            end_date TEXT NOT NULL,
            cost REAL NOT NULL,
            status TEXT NOT NULL,  -- 'pending', 'approved', 'rejected', 'cancelled'
            FOREIGN KEY (car_id) REFERENCES cars(id),
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    ''')

    # Check if the cars table is empty
    cursor.execute("SELECT COUNT(*) FROM cars")
    if cursor.fetchone()[0] == 0:
        # Insert initial car data
        initial_cars = [
            (1, "Toyota", "Corolla", 2020, 20000, 20.0, True, 2, 30),
            (2, "Honda", "Civic", 2019, 30000, 15.0, True, 3, 25),
            (3, "Ford", "Focus", 2021,45000, 25.0, True, 1, 20),
            (4, "Chevrolet", "Cruze",2022, 28000, 16.0, True, 5, 40),
            (5, "Nissan", "Sentra", 2020, 27000, 17.0, True, 2, 30)
        ]

        cursor.executemany('''
            INSERT INTO cars (id, make, model, year, mileage, price_per_day, available_now, min_rental_days, max_rental_days)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ? )
        ''', initial_cars)
        print("Initial car data inserted into the database.")

    conn.commit()
    conn.close()

# # Call this function when you run the system to ensure the database is ready
# initialize_database()
