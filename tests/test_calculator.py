from unittest import TestCase, mock
from unittest.mock import patch
import src
from src.calculator import Calculator
from mock import Mock
from mockito import *


class TestCalculator(TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_sum_without_mocking(self):
        calculator = Calculator()
        actual = calculator.sum(2, 4)
        self.assertEqual(6, actual)

    def test_sum_with_mocking(self):
        calculator = Mock()
        with patch('src.calculator.Calculator',attr_or_replacement=True):
            when(calculator).sum(2,4).thenReturn(1)
            when(calculator).sum(1,1).thenReturn(10)# calling the sum method but the mocked version will actually get called
        expected1 = 1   # expected is 1 because we are expecting 1 as output from sum method even though sum of 2 & 4 is 6.

        self.assertEqual(expected1, calculator.sum(2,4))
        expected10 = 10
        self.assertEqual(expected10, calculator.sum(1,1))
