class AirCondition:
    def __init__(self):
        self.__is_On = False
        self.increase_temp = int
        self.decrease_temp = int
        
    def set_is_off(self, is_off):
        self.__is_On = False
        
    def get_is_off(self):
        return self.__is_On

    def air_condition_is_off(self):
        self.__is_On = False

    def air_condition_is_on(self):
        self.__is_On = True
    


    