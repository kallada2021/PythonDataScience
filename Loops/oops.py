class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius
    
    @property
    def celsius(self):
        return self._celsius
    
    @celsius.setter
    def celsius(self, value):
        if value < -273.5:
            raise ValueError("Temperature below absolute zero!")
        self._celsius = value
        return self._celsius
    
    @property
    def fahrenheit(self):
        return (self.celsius * 9/5) + 32

# Using properties
temp = Temperature(25)
print(temp.celsius)     # Output: 25
print(temp.fahrenheit)  # Output: 77.0
temp.celsius = -30
print(temp.celsius)     # Output: 30
print(temp.fahrenheit)  # Output: 86.0