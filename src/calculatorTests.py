import unittest
from Calculator import Calculator


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_addition(self):
        self.assertEqual(self.calculator.add(5, 5), 10.0)

    def test_subtraction(self):
        self.assertEqual(self.calculator.subtract(5, 5), 0.0)

    def test_multiplication(self):
        self.assertEqual(self.calculator.multiply(5, 5), 25.0)

    def test_division(self):
        self.assertEqual(self.calculator.divide(5, 5), 1.0)


if __name__ == '__main__':
    unittest.main()
