from pytest import raises, approx
from vector import Vector

def test_valid_init():
    v1 = Vector(1,2)
    assert v1.numbers == (1,2)

def test_negative_valid_init():
    v2 = Vector(-1,-3)
    assert v2.numbers == (-1,-3)

def test_str_init_fails():
    with raises(TypeError):
        Vector(1,"2")

def test_len():
    vectors = (Vector(1,2,3),Vector(1,2),Vector(1))
    expected_len = (3,2,1)
    for a, b in zip(vectors,expected_len):
        assert len(a) == b

def test_vector_norm_valid():
    v1 = Vector(1,2)
    assert abs(v1) == 5**0.5

def test_empty_vector_fail():
    with raises(ValueError):
        Vector()
