class Bike:

    def __init__(self):
        self.gear = 1
        self.speed = 0
        self.__is_on = False

    def get_is_on(self):
        return self.__is_on

    def turn_bike_on(self):
        self.__is_on = True

    def turn_bike_off(self):
        self.__is_on = False

    def set_gear(self):
        if self.__is_on:
            if 0 >= self.get_current_speed() <= 20:
                self.gear = 1
            elif 21 >= self.get_current_speed() <= 30:
                self.gear = 2
            elif 31 >= self.get_current_speed() <= 40:
                self.gear = 3
            elif self.get_current_speed() > 40:
                self.gear = 4

    def accelerate(self):
        if self.get_is_on():
            if self.gear == 1:
                self.speed += 1
            elif self.gear == 2:
                self.speed += 2
            elif self.gear == 3:
                self.speed += 3
            elif self.gear == 4:
                self.speed += 4

        self.set_gear()

    def get_current_speed(self):
        print(self.speed)
        return self.speed

    def get_current_gear(self):
        return self.gear
