class Television:
    def __init__(self):
        self.is_Off = True
        self.channel = int
        self.volume_lowest = int

    def television_isOff(self):
        return self.is_Off

    def television_is_turn_on(self):
        self.is_Off = False
        return  self.is_Off

    def television_isOn(self):
        self.is_Off = False
        self.channel = 1
        self.volume_lowest = 1
        return self.is_Off

    def television_has_channels(self):
        return self.channel

    def set_channel(self, channel):
        self.channel = channel
        return self.channel

    def get_channel(self):
            return self.channel

    def television_channel_not_less_than_one_or_above_hundred(self, channel):
        if channel < 1 or channel > 100:
            raise ValueError("Channel must be between 1 and 100")
        else :
            return self.channel

    def television_change_channel(self , channel):
        self.channel = channel + 1
        return self.channel

    def set_volume(self, volume_lowest):
        self.volume_lowest = volume_lowest
        return self.volume_lowest

    def get_volume(self):
            return self.volume_lowest

    def television_has_volume(self):
        return self.volume_lowest

    def television_has_volumeUp(self, volume_lowest):
        self.volume_lowest = volume_lowest + 1
        return self.volume_lowest

    def television_has_volumeDown(self, volume_lowest):
        if volume_lowest > 1 :
            self.volume_lowest -= 1
        else :
            raise ValueError("Volume must above 1 to increase")



#             self.is_on = False
#             return self.is_on
#
#
#     def television_is_turn_On(self):
#         self.is_on = True
#         return self.is_on
#
#
#     def television_isOn(self):
#         self.is_on = True
#         return self.is_on
#
#     def television_is_on_channel1(self):
#             if self.channel == 1:
#                 return self.channel
#
#
#     def television_channels(self, channel):
#         if channel < 1 or channel > 100:
#             raise ValueError("Channel must be between 1 and 100")
#         else :
#             self.channel = channel
#
#
#
#
#     def television_channel_cannot_increase_when_isOff(self):
#         if self.is_on == False:
#             raise ValueError("Channel can't be increased")
#
#
#
#
# def television_channels(param):
#     return None