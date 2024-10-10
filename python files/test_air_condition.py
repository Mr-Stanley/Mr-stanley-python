import unittest

from tasks.air_condition import AirCondition


class TestAirCondition(unittest.TestCase):

    def test_that_air_condition_is_off(self):
        air_condition = AirCondition()
        air_condition.air_condition_is_off()
        self.assertFalse(air_condition.air_condition_is_on())

    def test_that_air_condition_is_on(self):
        air_condition = AirCondition()
        air_condition.air_condition_is_off()
        self.assertFalse(air_condition.air_condition_is_on())
        air_condition.air_condition_is_on()
        self.assertTrue(air_condition.air_condition_is_on())



