import unittest

from tasks.bike_task import Bike


class TestBikeTask(unittest.TestCase):

    def test_bike_is_off_i_turn_it_on(self):
        bike_task = Bike()
        given = bike_task.get_is_on()
        self.assertFalse(given)
        bike_task.turn_bike_on()
        when = bike_task.get_is_on()
        self.assertTrue(when)

    def test_that_bike_is_on_i_turn_it_off(self):
        bike_task = Bike()
        bike_task.turn_bike_on()
        given = bike_task.get_is_on()
        self.assertTrue(given)
        bike_task.turn_bike_off()
        when = bike_task.get_is_on()
        self.assertFalse(when)

    def test_that_bike_is_on_and_in_gear_one_i_accelerate_speed_is_15(self):
        bike_task = Bike()
        bike_task.turn_bike_on()
        given = bike_task.get_is_on()
        self.assertTrue(given)
        for index in range(15):
            bike_task.accelerate()
        current_gear = bike_task.get_current_gear()
        self.assertEqual(1, current_gear)

        bike_task.accelerate()
        current_speed = bike_task.get_current_speed()
        self.assertEqual(16, current_speed)

    def test_that_bike_is_on_and_in_gear_two_and_speed_is_21_i_accelerate_speed_is_23(self):
        bike_task = Bike()
        bike_task.turn_bike_on()
        given = bike_task.get_is_on()
        self.assertTrue(given)
        for index in range(21):
            bike_task.accelerate()
        current_gear = bike_task.get_current_gear()
        self.assertEqual(2, current_gear)

        bike_task.accelerate()
        current_speed = bike_task.get_current_speed()
        self.assertEqual(23, current_speed)

    def test_that_bike_is_on_and_in_gear_three_and_speed_is_31_i_accelerate_speed_is_34(self):
        bike_task = Bike()
        bike_task.turn_bike_on()
        given = bike_task.get_is_on()
        self.assertTrue(given)
        for index in range(33):
            bike_task.accelerate()
        current_gear = bike_task.get_current_gear()
        self.assertEqual(3, current_gear)

        bike_task.accelerate()
        current_speed = bike_task.get_current_speed()
        self.assertEqual(36, current_speed)


    def test_that_bike_is_on_and_in_gear_four_and_speed_is_41_i_accelerate_speed_is_45(self):
        bike_task = Bike()
        bike_task.turn_bike_on()
        given = bike_task.get_is_on()
        self.assertTrue(given)
        for index in range(41):
            bike_task.accelerate()
        current_gear = bike_task.get_current_gear()
        self.assertEqual(4, current_gear)

        bike_task.accelerate()
        current_speed = bike_task.get_current_speed()
        self.assertEqual(45, current_speed)


