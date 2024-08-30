import shape_math

def test_square():
    assert shape_math.square(2) == 4
    assert shape_math.square(3) == 9

def test_cube():
    assert shape_math.cube(2) == 8
    assert shape_math.cube(3) == 27

def test_add():
    assert shape_math.add(2, 3) == 5
    assert shape_math.add(-1, 1) == 0

def test_subtract():
    assert shape_math.subtract(5, 3) == 2
    assert shape_math.subtract(2, 5) == -3

def test_multiply():
    assert shape_math.multiply(2, 3) == 6
    assert shape_math.multiply(-1, 5) == -5

def test_divide():
    assert shape_math.divide(6, 3) == 2
    try:
        shape_math.divide(1, 0)
    except ValueError as e:
        assert str(e) == "Cannot divide by zero!"

def test_power():
    assert shape_math.power(2, 3) == 8
    assert shape_math.power(5, 0) == 1

def test_mod():
    assert shape_math.mod(5, 3) == 2
    assert shape_math.mod(10, 2) == 0

def test_factorial():
    assert shape_math.factorial(5) == 120
    assert shape_math.factorial(0) == 1
    try:
        shape_math.factorial(-1)
    except ValueError as e:
        assert str(e) == "Cannot calculate factorial of a negative number!"



