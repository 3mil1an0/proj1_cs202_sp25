import unittest
import math
from proj1 import *
#proj1.py should contain your data class and function definitions
#these do not contribute positivly to your grade. 
#but your grade will be lowered if they are missing

class TestRegionFunctions(unittest.TestCase):

    def setUp(self):
        pass

    def test_holder(self):
        pass

#-------------Emissions per capita
def test_emissions_per_capita_normal(self):
    result = emissions_per_capita(NYC)
    self.assertAlmostEqual(result, 58000000.0 / 8600000, places = 4)

def test_emissions_per_capita_zero_pop(self):
    result = emissions_per_capita(Tyrrhenian_Sea)
    self.assertAlmostEqual(result, 0.0, places = 4)

#-------------Area
def test_area_positive(self):
    result = area(NYC.region.rect)
    self.assertGreater(result, 0)

def test_area_wraparound(self):
    wrap_rect = GlobeRect(lo_lat= 0.0, hi_lat= 10.0, west_long = 170.0, east_long= -170.0)
    result = area(wrap_rect)
    self.assertGreater(result, 0)

#--------------emissions per square km
def test_emissions_per_square_km_normal(self):
    result = emissions_per_square_km(NYC)
    self.assertGreater(result, 0)

def test_emissions_per_square_km_ocean(self):
    result = emissions_per_square_km(Tyrrhenian_Sea)
    self.assertGreater(result,0)

#-----------------densest
def test_densest_single(self):
    result = densest([NYC])
    self.assertEqual(result, "NYC State")

def test_densest_multiple(self):
    result = densest(region_conditions)
    self.assertIsInstance(result,str)

#----------------- proect conditon
def test_project_condition_zero_years(self):
        result = project_condition(NYC, 0)
        self.assertEqual(result, NYC)

def test_project_condition_year_increases(self):
        result = project_condition(NYC, 10)
        self.assertEqual(result.year, 2026 + 10)

def test_project_condition_pop_grows(self):
        result = project_condition(NYC, 10)
        self.assertGreater(result.pop, NYC.pop)

def test_project_condition_forest_shrinks(self):
        result = project_condition(Moscow, 10)
        self.assertLess(result.pop, Moscow.pop)


if __name__ == '__main__':
    unittest.main()
