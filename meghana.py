.
def calculate_sum(numbers):
    return sum(numbers)

def calculate_average(numbers):
    return sum(numbers) / len(numbers)

def main():
    numbers = [10, 20, 30, 40, 50]
    print("Sum:", calculate_sum(numbers))
    print("Average:", calculate_average(numbers))

if __name__ == "__main__":
    main()
``'

**(link unavailable)**
python
def find_max(numbers):
    return max(numbers)

def find_min(numbers):
    return min(numbers)

def main():
    numbers = [10, 20, 30, 40, 50]
    print("Max:", find_max(numbers))
    print("Min:", find_min(numbers))

if _name_ == "_main_":
    main()


*(link unavailable)*

import unittest
from program1 import calculate_sum, calculate_average

class TestProgram1(unittest.TestCase):
    def test_calculate_sum(self):
        numbers = [1, 2, 3, 4, 5]
        self.assertEqual(calculate_sum(numbers), 15)

    def test_calculate_average(self):
        numbers = [1, 2, 3, 4, 5]
        self.assertEqual(calculate_average(numbers), 3)

if _name_ == "_main_":
    unittest.main()


*(link unavailable)*

import unittest
from program2 import find_max, find_min

class TestProgram2(unittest.TestCase):
    def test_find_max(self):
        numbers = [1, 2, 3, 4, 5]
        self.assertEqual(find_max(numbers), 5)

    def test_find_min(self):
        numbers = [1, 2, 3, 4, 5]
        self.assertEqual(find_min(numbers), 1)

if _name_ == "_main_":
    unittest.main()
```

Run the test scripts using the commands:

python (link unavailable)
python (link unavailable)

If all tests pass, your programs are working correctly.

Commit and push your code to the repository:

git add .
git commit -m "Completed Python coding assessment"
git push
