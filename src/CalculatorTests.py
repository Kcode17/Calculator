import unittest
from Calculator import Calculator
from CsvReader import CsvReader
from pprint import pprint


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_addition(self):
        print("Unit Test for Addition")
        test_data = CsvReader('/src/csvTestData/Unit Test Addition.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_subtraction(self):
        print("Unit Test for Subtraction")
        test_data = CsvReader('/src/csvTestData/Unit Test Subtraction.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_multiplication(self):
        print("Unit Test for Multiplication")
        test_data = CsvReader('/src/csvTestData/Unit Test Multiplication.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.multiply(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_division(self):
        print("Unit Test for Division")
        test_data = CsvReader('/src/csvTestData/Unit Test Division.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.divide(row['Value 1'], row['Value 2']), float(row['Result']))
            self.assertEqual(self.calculator.result, float(row['Result']))

    def test_square(self):
        print("Unit Test for Square")
        test_data = CsvReader('/src/csvTestData/Unit Test Square.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.square(row['Value 1']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_squareroot(self):
        print("Unit Test for Square Root")
        test_data = CsvReader('/src/csvTestData/Unit Test Square Root.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.squareroot(row['Value 1']), round(float(row['Result']), 8))
            self.assertEqual(self.calculator.result, round(float(row['Result']), 8))


if __name__ == '__main__':
    unittest.main()
