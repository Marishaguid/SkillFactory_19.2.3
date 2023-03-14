import pytest
from app.calculator import Calc


class TestCalc:

    def setup(self):
        self.calc = Calc

    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_division_calculate_correctly(self):
        assert self.calc.division(self, 6, 3) == 2

    def test_subtraction_calculate_correctly(self):
        assert self.calc.subtraction(self, 8, 2) == 6

    def test_adding_calculate_correctly(self):
        assert self.calc.adding(self, 4, 3) == 7
