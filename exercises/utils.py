from numbers import Number

def validate_positive_number(value) -> None:
    if not isinstance(value, Number):
        raise TypeError(f"value should be int or float not {type(value)}")
    if value < 0:
        raise ValueError(f"value can't be negative. Your value {value} is negative") 