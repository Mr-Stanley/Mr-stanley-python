import unittest

from tasks import television
from tasks.television import Television


class TestTelevision(unittest.TestCase):

    def test_television_isOff(self):
        television = Television()
        television.television_isOff()
        self.assertTrue(television.television_isOff())

    def test_that_television_can_turn_On(self):
        television = Television()
        self.assertTrue(television.television_isOff())
        television.television_is_turn_on()
        self.assertFalse(television.television_isOff())

    def test_that_television_isOn(self):
        television = Television()
        self.assertTrue(television.television_isOff())
        television.television_isOn()
        self.assertFalse(television.television_isOff())

    def test_that_television_has_channels(self):
        television = Television()
        television.television_is_turn_on()
        self.assertFalse(television.television_isOff())
        television.television_has_channels()
        self.assertTrue(television.television_has_channels())

    def test_that_television_channels_is_not_less_than_one_or_above_hundred(self):
        television = Television()
        self.assertTrue(television.television_has_channels())
        self.assertRaises(ValueError, television.television_channel_not_less_than_one_or_above_hundred, 0)

    def test_that_television_channel_can_increase_or_decrease(self):
        television = Television()
        self.assertFalse(television.television_isOn())
        self.assertEqual(television.get_channel(), 1)
        television.television_change_channel(2)
        self.assertEqual(television.get_channel(), 3)

    def test_that_television_has_volume(self):
        television = Television()
        television.television_is_turn_on()
        self.assertFalse(television.television_isOff())
        television.television_has_volume()
        self.assertTrue(television.television_has_volume())

    def test_that_television_volume_can_increase(self):
        television = Television()
        television.television_isOn()
        self.assertFalse(television.television_isOff())
        self.assertEqual(television.get_volume(), 1)
        television.television_has_volumeUp(2)
        self.assertEqual(television.get_volume(), 3)

    def test_that_television_volume_can_decrease(self):
        television = Television()
        television.television_isOn()
        self.assertFalse(television.television_isOff())
        television.volume_lowest(1)
        television.television_has_volumeDown(1)
        self.assertRaises(ValueError, television.volume_lowest, 0)






