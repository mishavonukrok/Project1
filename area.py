import math

def circle(radius_str):
    try:
        radius = float(radius_str)
    except ValueError:
        raise ValueError("Enter numeric values")

    if radius <= 0:
        raise TypeError("Values must be positive")
    return round(math.pi * radius * radius, 10)

def square(side_str):
    try:
        side = float(side_str)
    except ValueError:
        raise ValueError("Enter numeric values")

    if side <= 0:
        raise TypeError("Values must be positive")
    return round(side * side, 10)

def rectangle(length_str, width_str):
    try:
        length = float(length_str)
        width = float(width_str)
    except ValueError:
        raise ValueError("Enter numeric values")

    if length <= 0 or width <= 0:
        raise TypeError("Values must be positive")
    return round(length * width, 10)

def triangle(base_str, height_str):
    try:
        base = float(base_str)
        height = float(height_str)
    except ValueError:
        raise ValueError("Enter numeric values")

    if base <= 0 or height <= 0:
        raise TypeError("Values must be positive")
    return round(0.5 * base * height, 10)
