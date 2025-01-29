import sqlite3

DB_FILE = "car_rental.db"


class User:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, user_id=None, username=None, password=None, role=None):
        if not hasattr(self, '_initialized'):
            self.user_id = user_id   # used by booking
            self.role = role      # used by car_rental_system
            self._initialized = True

            self.username = username
            # self.password = password


    def check_username_availability(self, cursor):
        # Check if the username already exists in the database
        cursor.execute("SELECT * FROM users WHERE username = ?", (self.username,))
        existing_user = cursor.fetchone()

        # handles the same username
        if existing_user:
            print("This username is already taken. Please choose another.")
            raise ValueError  # Raise an exception if username is taken


    def register_user(self):
        print("\nRegister New User:")
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        # Ask for username, password until username is available
        while True:
            self.username = input("Enter username: ")
            try:
                self.check_username_availability(cursor)    # Check if username is available
            except ValueError:
                continue      # Username is taken, continue the loop
            else:
                print(f"Username {self.username} is available!")
                break  # Exit the loop if username is available

        password = input("Enter password: ")

        # Ask the user to choose a role: admin or customer
        while True:
            role = input("Enter role (admin/customer): ").lower()
            if role in ['admin', 'customer']:
                break
            else:
                print("Invalid role! Please choose either 'admin' or 'customer'.")

        # Insert the new user into the database
        cursor.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
                       (self.username, password, role))
        conn.commit()
        print(f"User '{self.username}' registered successfully!")

        conn.close()


    def login_user(self):
        """ Ask user for input. If username and password is correct, initialized the role attribute"""
        print("\nLogin:")
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()

        # Ask for username and password
        username = input("Enter username: ")
        password = input("Enter password: ")

        # get username and password in the database
        cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
        user = cursor.fetchone()

        #Check if username and password exists ,truthy or falsy
        if user:
            self.user_id = user[0] #rinitialize singleton attribute user_id
            self.role = user[3]    #initialize singleton attribute user_role
            print(f"Welcome back, {username}!")
            #Initialialized attributes from the database
            #return User(user_id=user[0], username=user[1], password=user[2], role=user[3])  # Return User object
            return True

        else:
            print("Invalid username or password. Please try again.")
            conn.close()
            return False
