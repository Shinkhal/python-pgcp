class SmartThermostat:
    MIN_TEMP = 10.0
    MAX_TEMP = 35.0

    def __init__(self, appliance_name, initial_temp=22.0):
        self.__appliance_name = appliance_name

        if self.MIN_TEMP <= initial_temp <= self.MAX_TEMP:
            self.__target_temp = initial_temp
        else:
            self.__target_temp = 22.0

    @property
    def target_temp(self):
        return self.__target_temp

    @target_temp.setter
    def target_temp(self, new_temp):
        if self.MIN_TEMP <= new_temp <= self.MAX_TEMP:
            self.__target_temp = new_temp
        else:
            raise ValueError(
                "Temperature must be between 10.0 and 35.0 degrees."
            )

    @property
    def appliance_name(self):
        return self.__appliance_name


# Example
thermostat = SmartThermostat("Living Room AC", 24.0)

print(thermostat.appliance_name)
print(thermostat.target_temp)

thermostat.target_temp = 28.0

print(thermostat.target_temp)

try:
    thermostat.target_temp = 5.0
except ValueError as e:
    print(e)