import pytest
from app.calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator


    def test_multiply_calculate_correctly(self):
        assert self.calc.multiply(self, 3, 2) == 6


    def test_division_calculate_correctly(self):
        assert self.calc.multiply(self, 6, 2) == 3


    def test_subtraction_calculate_correctly(self):
        assert self.calc.multiply(self, 6, 2) == 4


    def test_adding_calculate_correctly(self):
        assert self.calc.multiply(self, 4, 2) == 6

