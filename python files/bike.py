class Bike :
    def __init__(self):
        self.__is_off = True
        self.gear = 0
        self.speed = 0
        self.accelerator = 0


    def set_is_off(self):
        self.__is_off = True

    def get_is_off(self):
        return self.__is_off

    def bike_is_off(self):
        return self.__is_off

    def bike_is_turned_on(self):
        self.__is_off = False
        return self.__is_off

    def bike_is_on(self):
        self.__is_off = False
        return self.__is_off

    def set_gear(self, gear):
        if self.speed >= 0 and self.speed <= 20:
            self.gear = 1
        elif self.speed >= 21 and self.speed <= 30:
            self.gear = 2
        elif self.speed >= 31 and self.speed <= 40:
            self.gear = 3
        else :
            self.speed >= 41
            self.gear <= 4
        self.gear = gear

    def get_gear(self):
        return self.gear

    def bike_has_gear(self):
        self.gear = True
        return self.gear

    def set_accelerator(self, accelerator):
        if self.gear == 1:
            self.accelerator += 1
        elif self.gear == 2:
            self.accelerator += 2
        elif self.gear == 3:
            self.accelerator += 3
        else :
            self.accelerator += 4
        return self.accelerator

    def get_accelerator(self):
        return self.accelerator

    def bike_can_accelerate(self):
         self.accelerator +=1

    def set_speed(self, speed):
        if self.speed >= 0 and self.speed <= 20:
            self.speed += 1
            self.accelerator +=1
        elif self.speed >= 21 and self.speed <= 30:
            self.speed += 2
            self.accelerator += 2
        elif self.speed >= 31 and self.speed <= 40:
            self.speed += 3
            self.accelerator += 3
        else :
            self.speed >= 41
            self.speed += 4
            self.accelerator += 4

        self.speed = speed

    def get_speed(self):
        return self.speed

    def bike_can_speed_when_it_accelerates(self):
        return self.speed

    def bike_accelerator_increases_by_1_when_bike_is_in_gear_one(self):
        self.__is_off = False
        self.set_gear(1)
        self.accelerator +=1
        return self.accelerator

    def bike_accelerator_increases_by_2_when_bike_is_in_gear_two(self):
        self.__is_off = False
        self.set_gear(2)
        self.accelerator +=2
        return self.accelerator

    def bike_accelerator_increases_by_3_when_bike_is_in_gear_three(self):
        self.__is_off = False
        self.set_gear(3)
        self.accelerator +=3
        return self.accelerator

    def bike_accelerator_increases_by_4_when_bike_is_in_gear_four(self):
        self.__is_off = False
        self.set_gear(3)
        self.accelerator +=4
        return self.accelerator

    def bike_decelerator_decreases_by_4_when_bike_is_in_gear_four(self):
        self.__is_off = False
        self.set_gear(4)
        self.accelerator -= 4
        return self.accelerator

    def bike_decelerator_decreases_by_3_when_bike_is_in_gear_three(self):
        self.__is_off = False
        self.set_gear(3)
        self.accelerator -= 3
        return self.accelerator

    def bike_decelerator_decreases_by_2_when_bike_is_in_gear_two(self):
        self.__is_off = False
        self.set_gear(2)
        self.accelerator -= 2
        return self.accelerator

    def bike_decelerator_decreases_by_1_when_bike_is_in_gear_one(self):
        self.__is_off = False
        self.set_gear(1)
        self.accelerator -= 1
        return self.accelerator

    def increase_speed_by_4(self):
        self.__is_off = False
        if self.gear == 4 :
            self.speed += 4
        return self.speed

    def increase_speed_by_3(self):
        self.__is_off = False
        if self.gear == 3:
            self.speed += 3
            return self.speed

    def increase_speed_by_2(self):
        self.__is_off = False
        if self.gear == 2:
            self.speed += 2
            return self.speed

    def increase_speed_by_1(self):
        self.__is_off = False
        if self.gear == 1:
            self.speed += 1
            return self.speed













