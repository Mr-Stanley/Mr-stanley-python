import unittest

from tasks import bike
from tasks.bike import Bike


class TestBike(unittest.TestCase):

    def test_that_bike_is_off(self):
        bike = Bike()
        bike.bike_is_off()
        self.assertTrue(bike.bike_is_off())

    def test_that_bike_can_be_turned_on(self):
        bike = Bike()
        bike.bike_is_off()
        bike.bike_is_turned_on()
        self.assertFalse(bike.bike_is_off())

    def test_that_bike_is_on(self):
        bike = Bike()
        bike.bike_is_off()
        bike.bike_is_on()
        self.assertFalse(bike.bike_is_off())

    def test_that_bike_has_gear(self):
        bike = Bike()
        bike.bike_is_on()
        bike.bike_has_gear()
        self.assertTrue(bike.bike_has_gear())

    def test_that_bike_can_can_accelerate_when_turned_on(self):
        bike = Bike()
        bike.bike_is_on()
        bike.set_gear(1)
        initial_accelerator = bike.get_accelerator()
        bike.bike_can_accelerate()
        expected_accelerator = initial_accelerator + 1
        self.assertEqual(expected_accelerator,bike.get_accelerator())


    def test_that_accelerator_increases_by_1_when_bike_is_in_gear_one(self):
        bike = Bike()
        bike.bike_is_on()
        bike.set_gear(1)
        initial_accelerator = bike.get_accelerator()
        expected_accelerator = initial_accelerator +1
        bike.bike_accelerator_increases_by_1_when_bike_is_in_gear_one()
        self.assertEqual(expected_accelerator, bike.get_accelerator())

    def test_that_accelerator_increases_by_2_when_bike_is_in_gear_two(self):
        bike = Bike()
        bike.bike_is_on()
        bike.set_gear(2)
        initial_accelerator = bike.get_accelerator()
        expected_accelerator = initial_accelerator +2
        bike.bike_accelerator_increases_by_2_when_bike_is_in_gear_two()
        self.assertEqual(expected_accelerator, bike.get_accelerator())

    def test_that_accelerator_increases_by_3_when_bike_is_in_gear_three(self):
        bike = Bike()
        bike.bike_is_on()
        bike.set_gear(3)
        initial_accelerator = bike.get_accelerator()
        expected_accelerator = initial_accelerator +3
        bike.bike_accelerator_increases_by_3_when_bike_is_in_gear_three()
        self.assertEqual(expected_accelerator, bike.get_accelerator())

    def test_that_accelerator_increases_by_4_when_bike_is_in_gear_four(self):
        bike = Bike()
        bike.bike_is_on()
        bike.set_gear(4)
        initial_accelerator = bike.get_accelerator()
        expected_accelerator = initial_accelerator +4
        bike.bike_accelerator_increases_by_4_when_bike_is_in_gear_four()
        self.assertEqual(expected_accelerator, bike.get_accelerator())

    def test_that_bike_decelerator_decreases_by_4_when_bike_is_in_gear_four(self):
        bike = Bike()
        bike.bike_is_on()
        bike.set_gear(4)
        initial_accelerator = bike.get_accelerator()
        expected_accelerator = initial_accelerator -4
        bike.bike_decelerator_decreases_by_4_when_bike_is_in_gear_four()
        self.assertEqual(expected_accelerator, bike.get_accelerator())

    def test_that_bike_decelerator_decreases_by_3_when_bike_is_in_gear_three(self):
        bike = Bike()
        bike.bike_is_on()
        bike.set_gear(3)
        initial_accelerator = bike.get_accelerator()
        expected_accelerator = initial_accelerator -3
        bike.bike_decelerator_decreases_by_3_when_bike_is_in_gear_three()
        self.assertEqual(expected_accelerator, bike.get_accelerator())

    def test_that_bike_decelerator_decreases_by_2_when_bike_is_in_gear_two(self):
        bike = Bike()
        bike.bike_is_on()
        bike.set_gear(2)
        initial_accelerator = bike.get_accelerator()
        expected_accelerator = initial_accelerator - 2
        bike.bike_decelerator_decreases_by_2_when_bike_is_in_gear_two()
        self.assertEqual(expected_accelerator, bike.get_accelerator())

    def test_that_bike_decelerator_decreases_by_1_when_bike_is_in_gear_one(self):
        bike = Bike()
        bike.bike_is_on()
        bike.set_gear(1)
        initial_accelerator = bike.get_accelerator()
        expected_accelerator = initial_accelerator - 1
        bike.bike_decelerator_decreases_by_1_when_bike_is_in_gear_one()
        self.assertEqual(expected_accelerator, bike.get_accelerator())

    def test_that_speed_increases_by_4_when_bike_is_in_gear_four(self):
        bike = Bike()
        bike.bike_is_on()
        bike.set_gear(4)
        initial_speed = bike.get_speed()
        bike.increase_speed_by_4()
        expected_speed = initial_speed + 4
        self.assertEqual(expected_speed, bike.get_speed())

    def test_that_speed_increases_by_3_when_bike_is_in_gear_three(self):
        bike = Bike()
        bike.bike_is_on()
        bike.set_gear(3)
        initial_speed = bike.get_speed()
        bike.increase_speed_by_3()
        expected_speed = initial_speed + 3
        self.assertEqual(expected_speed, bike.get_speed())

    def test_that_speed_increases_by_2_when_bike_is_in_gear_two(self):
        bike = Bike()
        bike.bike_is_on()
        bike.set_gear(2)
        initial_speed = bike.get_speed()
        bike.increase_speed_by_2()
        expected_speed = initial_speed + 2
        self.assertEqual(expected_speed, bike.get_speed())

    def test_that_speed_increases_by_1_when_bike_is_in_gear_one(self):
        bike = Bike()
        bike.bike_is_on()
        bike.set_gear(1)
        initial_speed = bike.get_speed()
        bike.increase_speed_by_1()
        expected_speed = initial_speed + 1
        self.assertEqual(expected_speed, bike.get_speed())











