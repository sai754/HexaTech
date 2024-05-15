# Testing

# Types of testing
# Performance testing
# Load Testing   (How much data)
# Stress Testing (How many users)
# Resilient Testing (How the app works even if something fails)
# Regression Testing (When the bug resurfaces)


# Testing Pyramid

# E2E testing - End to End testing (Written by QA) Selenium
# Integration testing
# Unit Test - written by dev

# Test Driven Development - Modern Approach
# 1. Write a failing test
# 2. Develop Production code that passes the test
# 3. Make the code as clean as possible

import unittest

def add(a,b):
    return a + b

class TestMyModule(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1,1),2)
    def test_negative_1(self):
        self.assertEqual(add(-1,1),0)
    def test_negative_2(self):
        self.assertEqual(add(-1,-1),-2)
    def test_add_decimal(self):
        self.assertEqual(add(1,1.1),2.1)

# setUp & tearDown
# setUp will automatically run before a testcase
# tearDown will automatically run after testcase
# AAA -> Arrange Act Assert

def adds_interest(accounts, rate):
    pass

class TestInterestModule(unittest.TestCase):
    # Setup: Arrange
    def setUp(self):
        print("Setup Ran...")
        self.accounts = [
            {
                "id": 1,
                "name": "John Doe",
                "email": "johndoe@example.com",
                "isActive": True,
                "balance": 150.75,
            },
            {
                "id": 2,
                "name": "Jane Smith",
                "email": "janesmith@example.com",
                "isActive": True,
                "balance": 500.50,
            },
            {
                "id": 3,
                "name": "Emily Jones",
                "email": "emilyjones@example.com",
                "isActive": True,
                "balance": 0.00,
            },
        ]
 
    def tearDown(self):
        print("TearDown : Clear cursor")
 
    def test_interest_rate_for_active_user(self):
        # Act
        output = adds_interest(self.accounts, 0.1)
        print("Test 1")
        # Assert
        self.assertEqual(add(1.2, 3.2), 4.4)
 
    def test_interest_rate_for_non_active_user(self):
        output = adds_interest(self.accounts, 0.1)
        print("Test 2")
        # self.assertEqual(output[1]["balance"], 500.5)



if __name__=="__main__":
    unittest.main()

  
