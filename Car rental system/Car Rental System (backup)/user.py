import sqlite3

DB_FILE = "car_rental.db"


class User:
    def __init__(self, user_id, username, password, role):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.role = role

    def get_role(self):
        return self.role

    @staticmethod
    def register_user():
        print("\nRegister New User:")
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        # Ask for username, password, and role
        username = input("Enter username: ")
        password = input("Enter password: ")

        # Ask the user to choose a role: admin or customer
        while True:
            role = input("Enter role (admin/customer): ").lower()
            if role in ['admin', 'customer']:
                break
            else:
                print("Invalid role! Please choose either 'admin' or 'customer'.")

        # Check if the username already exists in the database
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        existing_user = cursor.fetchone()

        if existing_user:
            print("This username is already taken. Please choose another.")
            conn.close()
            return None

        # Insert the new user into the database
        cursor.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
                       (username, password, role))
        conn.commit()
        print(f"User '{username}' registered successfully!")

        conn.close()

    @staticmethod
    def login_user():
        print("\nLogin:")
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        # Ask for username and password
        username = input("Enter username: ")
        password = input("Enter password: ")

        # Check if the user exists and the password is correct
        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        user = cursor.fetchone()

        # truthy or falsy values
        if user:
            print(f"Welcome back, {username}!")
            return User(user_id=user[0], username=user[1], password=user[2], role=user[3])  # Return User object
        else:
            print("Invalid username or password. Please try again.")
            conn.close()
            return None
