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
        test_data = CsvReader('/src/csvTestData/Unit_Test_Addition.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_subtraction(self):
        print("Unit Test for Subtraction")
        test_data = CsvReader('/src/csvTestData/Unit_Test_Subtraction.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_multiplication(self):
        print("Unit Test for Multiplication")
        test_data = CsvReader('/src/csvTestData/Unit_Test_Multiplication.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.multiply(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_division(self):
        print("Unit Test for Division")
        test_data = CsvReader('/src/csvTestData/Unit_Test_Division.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.divide(row['Value 1'], row['Value 2']), float(row['Result']))
            self.assertEqual(self.calculator.result, float(row['Result']))

    def test_square(self):
        self.assertEqual(self.calculator.square(5), 25.0)

    def test_squareroot(self):
        self.assertEqual(self.calculator.squareroot(100), 10.0)


if __name__ == '__main__':
    unittest.main()
