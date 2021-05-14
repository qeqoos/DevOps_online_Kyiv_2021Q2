import unittest
import calculator


class calculatorTests(unittest.TestCase):
    def test_add1(self):
        num1 = 228
        num2 = 1337
        result = calculator.Calculator.add(self, num1, num2)
        self.assertEqual(result, 1565)

    def test_add2(self):
        num1 = -0.2563
        num2 = 7362.0063
        result = calculator.Calculator.add(self, num1, num2)
        self.assertEqual(result, 7361.75)

    @unittest.expectedFailure
    def test_add_string(self):
        num1 = 4
        num2 = '0'
        result = calculator.Calculator.add(self, num1, num2)
        self.assertEqual(result, 4)

    def test_subtract1(self):
        num1 = 4
        num2 = 6
        result = calculator.Calculator.subtract(self, num1, num2)
        self.assertEqual(result, -2)

    def test_subtract2(self):
        num1 = 23842341
        num2 = 576523
        result = calculator.Calculator.subtract(self, num1, num2)
        self.assertEqual(result, 23265818)

    def test_subtract3(self):
        num1 = -235.34
        num2 = -536.87
        result = calculator.Calculator.subtract(self, num1, num2)
        self.assertEqual(result, 301.53)

    def test_multiply1(self):
        num1 = 4
        num2 = 6
        result = calculator.Calculator.multiply(self, num1, num2)
        self.assertEqual(result, 24)

    def test_multiply2(self):
        num1 = 1243
        num2 = 5736
        result = calculator.Calculator.multiply(self, num1, num2)
        self.assertEqual(result, 7129848)

    def test_multiply3(self):
        num1 = -0.346
        num2 = 25.1
        result = calculator.Calculator.multiply(self, num1, num2)
        self.assertEqual(result, -8.6846)

    @unittest.expectedFailure
    def test_divide_zero(self):
        num1 = 26835
        num2 = 0
        result = calculator.Calculator.divide(self, num1, num2)
        self.assertEqual(result, 5367.0, ZeroDivisionError)

    def test_divide2(self):
        num1 = -229342759.87
        num2 = -503717.9
        result = calculator.Calculator.divide(self, num1, num2)
        self.assertEqual(result, 455.3)

    def test_divide3(self):
        num1 = 0
        num2 = 0.2345
        result = calculator.Calculator.divide(self, num1, num2)
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()
