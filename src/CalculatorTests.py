import unittest
from Calculator import Calculator
from CsvReader import CsvReader


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_addition(self):
        test_data = CsvReader('/src/csvTestData/Unit_Test_Addition.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_subtraction(self):
        self.assertEqual(self.calculator.subtract(5, 5), 0.0)

    def test_multiplication(self):
        self.assertEqual(self.calculator.multiply(5, 5), 25.0)

    def test_division(self):
        self.assertEqual(self.calculator.divide(5, 5), 1.0)

    def test_square(self):
        self.assertEqual(self.calculator.square(5), 25.0)

    def test_squareroot(self):
        self.assertEqual(self.calculator.squareroot(100), 10.0)


if __name__ == '__main__':
    unittest.main()
