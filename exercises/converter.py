from numbers import Number
from utils import validate_positive_number

class UnitConverter:
    def __init__(self, value: int | float) -> None:
        self.value = value
    
    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, new_value):
        validate_positive_number(new_value)
        self._value = new_value

    def inch_to_cm(self):
        return 2.54 * self.value
    
    def foot_to_meter(self):
        return .3048 * self.value

#    def __repr__
test1 = UnitConverter(-5)

print(f"{test1.value}")

