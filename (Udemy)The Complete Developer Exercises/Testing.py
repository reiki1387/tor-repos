
# import unittest

# def add(a, b):
#     return a + b

# class TestAddFunction(unittest.TestCase):
#     def test_add_integers(self):
#         self.assertEqual(add(1, 2), 3)
    
#     def test_add_floats(self):
#         self.assertAlmostEqual(add(1.1, 2.2), 3.3, places=1)
    
#     def test_add_strings(self):
#         self.assertEqual(add('hello', ' world'), 'hello world')

# if __name__ == '__main__':
#     unittest.main()

# import pytest

# # test_sample.py
# def add(a, b):
#     return a + b

# def test_add_integers():
#     assert add(1, 2) == 3

# def test_add_strings():
#     assert add('hello', ' world') == 'hello world'

# if __name__ == '__main__':
#     pytest.main()




# import unittest

# class TestCookieBaking(unittest.TestCase):
#     def setUp(self):
#         print("\n🧑🍳 Preparing kitchen...")
#         self.oven_temp = 350
#         self.bowl = ["flour", "sugar", "eggs"]
#         self.cookie_sheet = []
    
#     def tearDown(self):
#         print("🧼 Cleaning up...")
#         self.bowl = []
#         self.cookie_sheet = []

#     def test_chocolate_chip(self):
#         print("Testing chocolate chip cookies...")
#         self.cookie_sheet.append("chocolate chip cookie")
#         self.assertEqual(len(self.cookie_sheet), 2)  #this will show error
    
#     def test_oatmeal_raisin(self):
#         print("Testing oatmeal raisin cookies...")
#         self.bowl.append("oats")
#         self.assertIn("oats", self.bowl)

# if __name__ == '__main__':
#     unittest.main(verbosity=2)



# import unittest
# import sqlite3

# class TestUserDatabase(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         """Create test database (runs once)"""
#         print("\n🔌 Connecting to database...")
#         cls.connection = sqlite3.connect(":memory:")
#         cls.cursor = cls.connection.cursor()
#         cls.cursor.execute("CREATE TABLE users (id INTEGER, name TEXT)")
    
#     @classmethod 
#     def tearDownClass(cls):
#         """Destroy test database (runs once)"""
#         print("\n❌ Disconnecting from database...")
#         cls.connection.close()
    
#     def setUp(self):
#         """Fresh data for each test"""
#         print("\n🆕 Inserting test user...")
#         self.cursor.execute("INSERT INTO users VALUES (1, 'TestUser')")
    
#     def tearDown(self):
#         """Clean data after each test"""
#         print("🧹 Clearing test data...")
#         self.cursor.execute("DELETE FROM users")
    
#     def test_user_count(self):
#         self.cursor.execute("SELECT COUNT(*) FROM users")
#         count = self.cursor.fetchone()[0]
#         self.assertEqual(count, 1)
    
#     def test_user_name(self):
#         self.cursor.execute("SELECT name FROM users WHERE id = 1")
#         name = self.cursor.fetchone()[0]
#         self.assertEqual(name, "TestUser")

# if __name__ == '__main__':
#     unittest.main()

# import unittest
# class TestCalculator(unittest.TestCase):
#     def setUp(self):
#         """Each test gets a fresh calculator"""
#         self.calc = Calculator()
    
#     def tearDown(self):
#         """Cleanup (not strictly needed here)"""
#         del self.calc
    
#     def test_addition(self):
#         self.assertEqual(self.calc.add(2, 3), 5)
    
#     def test_subtraction(self):
#         self.assertEqual(self.calc.subtract(5, 2), 3)


# import unittest

# class BankAccount:
#     def __init__(self):
#         self.balance = 0
#         self.transactions = []
    
#     def deposit(self, amount):
#         self.balance += amount
#         self.transactions.append(f"Deposit: +{amount}")
    
#     def withdraw(self, amount):
#         if amount > self.balance:
#             raise ValueError("Insufficient funds")
#         self.balance -= amount
#         self.transactions.append(f"Withdrawal: -{amount}")

# class TestBankAccount(unittest.TestCase):
#     def setUp(self):
#         """Fresh account for each test"""
#         print("\n🆕 Opening new account with $100 balance")
#         self.account = BankAccount()
#         self.account.deposit(100)  # Starting balance
    
#     def tearDown(self):
#         """Cleanup (not strictly necessary here but good practice)"""
#         print("🗑️ Closing account after test")
#         del self.account
    
#     def test_deposit(self):
#         self.account.deposit(50)
#         self.assertEqual(self.account.balance, 150)
#         self.assertEqual(len(self.account.transactions), 2)
    
#     def test_withdraw(self):
#         self.account.withdraw(30)
#         self.assertEqual(self.account.balance, 70)
#         self.assertIn("Withdrawal: -30", self.account.transactions)
    
#     def test_insufficient_funds(self):
#         with self.assertRaises(ValueError):
#             self.account.withdraw(200)

# if __name__ == '__main__':
#     unittest.main(verbosity=2)


# import unittest
# import json

# class WeatherServiceConfig:
#     def __init__(self, config_file):
#         with open(config_file) as f:    # 1. Open the file
#             self.config = json.load(f)  # 2. Parse JSON → Python dict
    
#     def validate(self):
#         required_keys = ['api_key', 'base_url', 'units']
#         return all(key in self.config for key in required_keys)

# class TestWeatherConfig(unittest.TestCase):
#     @classmethod
#     def setUpClass(cls):
#         """Load config once - expensive I/O operation"""
#         print("\n🌤️ Loading weather service configuration...")
#         cls.weather_config = WeatherServiceConfig("config.json")
    
#     @classmethod
#     def tearDownClass(cls):
#         """Cleanup"""
#         print("\n🌤️ Releasing weather config resources...")
#         del cls.weather_config
    
#     def test_api_key_present(self):
#         self.assertIn("api_key", self.weather_config.config)
    
#     def test_base_url_valid(self):
#         self.assertTrue(self.weather_config.config["base_url"].startswith("https://"))
    
#     def test_config_validation(self):
#         self.assertTrue(self.weather_config.validate())

# if __name__ == '__main__':
#     unittest.main(verbosity=2)


# import unittest

# # The class we want to test
# class BankAccount:
#     def __init__(self, account_holder, initial_balance=0):
#         self.account_holder = account_holder
#         self.balance = initial_balance
    
#     def deposit(self, amount):
#         if amount <= 0:
#             raise ValueError("Deposit amount must be positive")
#         self.balance += amount
#         return self.balance
    
#     def withdraw(self, amount):
#         if amount <= 0:
#             raise ValueError("Withdrawal amount must be positive")
#         if amount > self.balance:
#             raise ValueError("Insufficient funds")
#         self.balance -= amount
#         return self.balance
    
#     def get_balance(self):
#         return self.balance
    
#     def transfer(self, amount, target_account):
#         self.withdraw(amount)
#         target_account.deposit(amount)
#         return True


# # Our test class
# class TestBankAccount(unittest.TestCase):
#     # Class-level setup/teardown (run once for the whole class)
#     @classmethod
#     def setUpClass(cls):
#         print("\nSetting up test class...")
#         cls.default_holder = "John Doe"
    
#     @classmethod
#     def tearDownClass(cls):
#         print("\nTearing down test class...")
    
#     # Instance-level setup/teardown (run before/after each test method)
#     def setUp(self):
#         print("\nSetting up for a test...")
#         self.account = BankAccount(self.default_holder, 100)
#         self.target_account = BankAccount("Jane Smith", 50)
    
#     def tearDown(self):
#         print("Cleaning up after test...")
#         del self.account
#         del self.target_account
    
#     # Test methods
#     def test_initial_balance(self):
#         print("Running test_initial_balance...")
#         self.assertEqual(self.account.get_balance(), 100)
    
#     def test_deposit_positive_amount(self):
#         print("Running test_deposit_positive_amount...")
#         new_balance = self.account.deposit(50)
#         self.assertEqual(new_balance, 150)
#         self.assertEqual(self.account.get_balance(), 150)
    
#     def test_withdraw_positive_amount(self):
#         print("Running test_withdraw_positive_amount...")
#         new_balance = self.account.withdraw(30)
#         self.assertEqual(new_balance, 70)
#         self.assertEqual(self.account.get_balance(), 70)
    
#     def test_deposit_negative_amount_raises_error(self):
#         print("Running test_deposit_negative_amount_raises_error...")
#         with self.assertRaises(ValueError):
#             self.account.deposit(-10)
    
#     def test_withdraw_negative_amount_raises_error(self):
#         print("Running test_withdraw_negative_amount_raises_error...")
#         with self.assertRaises(ValueError):
#             self.account.withdraw(-10)
    
#     def test_withdraw_more_than_balance_raises_error(self):
#         print("Running test_withdraw_more_than_balance_raises_error...")
#         with self.assertRaises(ValueError):
#             self.account.withdraw(200)
    
#     def test_transfer_successful(self):
#         print("Running test_transfer_successful...")
#         result = self.account.transfer(30, self.target_account)
#         self.assertTrue(result)
#         self.assertEqual(self.account.get_balance(), 70)
#         self.assertEqual(self.target_account.get_balance(), 80)
    
#     def test_transfer_insufficient_funds(self):
#         print("Running test_transfer_insufficient_funds...")
#         with self.assertRaises(ValueError):
#             self.account.transfer(200, self.target_account)
    
#     @unittest.skip("Skipping this test for demonstration")
#     def test_skip_example(self):
#         self.fail("This test should be skipped")
    
#     # This test will fail on purpose to show failure output
#     def test_failure_example(self):
#         print("Running test_failure_example...")
#         self.assertEqual(self.account.deposit(10), 110)
#         self.assertEqual(self.account.deposit(20), 120)  # This will fail (should be 130)


# if __name__ == '__main__':
#     unittest.main(verbosity=2)  # verbosity=2 shows more detailed output


# test_bank_account.py
# import pytest

# class BankAccount:
#     def __init__(self, account_holder, initial_balance=0):
#         self.account_holder = account_holder
#         self.balance = initial_balance
    
#     def deposit(self, amount):
#         if amount <= 0:
#             raise ValueError("Deposit amount must be positive")
#         self.balance += amount
#         return self.balance
    
#     def withdraw(self, amount):
#         if amount <= 0:
#             raise ValueError("Withdrawal amount must be positive")
#         if amount > self.balance:
#             raise ValueError("Insufficient funds")
#         self.balance -= amount
#         return self.balance
    
#     def get_balance(self):
#         return self.balance
    
#     def transfer(self, amount, target_account):
#         self.withdraw(amount)
#         target_account.deposit(amount)
#         return True

# # Fixtures (replace setUp/tearDown)
# @pytest.fixture
# def default_account():
#     """Fresh account for each test with $100 balance"""
#     account = BankAccount("John Doe", 100)
#     yield account  # This is where the test runs
#     # Optional teardown (pytest handles cleanup automatically)

# @pytest.fixture
# def target_account():
#     return BankAccount("Jane Smith", 50)

# # Tests (no need for TestCase class)
# def test_initial_balance(default_account):
#     assert default_account.get_balance() == 100

# def test_deposit_positive_amount(default_account):
#     new_balance = default_account.deposit(50)
#     assert new_balance == 150
#     assert default_account.get_balance() == 150

# def test_withdraw_positive_amount(default_account):
#     new_balance = default_account.withdraw(30)
#     assert new_balance == 70
#     assert default_account.get_balance() == 70

# def test_deposit_negative_amount_raises_error(default_account):
#     with pytest.raises(ValueError, match="Deposit amount must be positive"):
#         default_account.deposit(-10)

# def test_transfer_successful(default_account, target_account):
#     result = default_account.transfer(30, target_account)
#     assert result is True
#     assert default_account.get_balance() == 70
#     assert target_account.get_balance() == 80

# # Parametrized test for multiple cases
# @pytest.mark.parametrize("amount,expected_balance", [
#     (10, 90),
#     (50, 50),
#     (100, 0),  # Edge case: emptying account
# ])
# def test_withdraw_various_amounts(default_account, amount, expected_balance):
#     default_account.withdraw(amount)
#     assert default_account.get_balance() == expected_balance



#PYTEST FIXTURE SCOPE MAPPING
import pytest

@pytest.fixture(scope="function")
def func_scope():
    print("\n[Fixture] function scope")
    return "function-scope"

@pytest.fixture(scope="class")
def class_scope():
    print("\n[Fixture] class scope")
    return "class-scope"

@pytest.fixture(scope="module")
def module_scope():
    print("\n[Fixture] module scope")
    return "module-scope"

@pytest.fixture(scope="session")
def session_scope():
    print("\n[Fixture] session scope")
    return "session-scope"


class TestGroupA:

    def test_a1(self, func_scope, class_scope, module_scope, session_scope):
        print("Running test_a1")

    def test_a2(self, func_scope, class_scope, module_scope, session_scope):
        print("Running test_a2")

class TestGroupB:

    def test_b1(self, func_scope, class_scope, module_scope, session_scope):
        print("Running test_b1")

#use pytest -s intead of this
# if __name__ == '__main__':
#     pytest.main()
