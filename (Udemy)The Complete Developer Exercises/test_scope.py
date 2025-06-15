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


#UNITTEST FIXTURE SCOPE MAPPING
# import unittest

# def setUpModule():
#     print("[unittest] Module setup")

# def tearDownModule():
#     print("[unittest] Module teardown")

# class TestExample(unittest.TestCase):

#     @classmethod
#     def setUpClass(cls):
#         print("[unittest] Class setup")

#     @classmethod
#     def tearDownClass(cls):
#         print("[unittest] Class teardown")

#     def setUp(self):
#         print("[unittest] Function setup")

#     def tearDown(self):
#         print("[unittest] Function teardown")

#     def test_one(self):
#         print("Running test_one")

#     def test_two(self):
#         print("Running test_two")


# if __name__ == '__main__':
#     unittest.main()