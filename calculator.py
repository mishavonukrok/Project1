import math

def circle_area(radius_str):
    try:
        radius = float(radius_str)
    except ValueError:
        raise ValueError("Enter numeric values")

    if radius <= 0:
        raise TypeError("Values must be positive")
    return round(math.pi * radius * radius, 10)

def square_area(side_str):
    try:
        side = float(side_str)
    except ValueError:
        raise ValueError("Enter numeric values")

    if side <= 0:
        raise TypeError("Values must be positive")
    return round(side * side, 10)

def rectangle_area(length_str, width_str):
    try:
        length = float(length_str)
        width = float(width_str)
    except ValueError:
        raise ValueError("Enter numeric values")

    if length <= 0 or width <= 0:
        raise TypeError("Values must be positive")
    return round(length * width, 10)

def triangle_area(base_str, height_str):
    try:
        base = float(base_str)
        height = float(height_str)
    except ValueError:
        raise ValueError("Enter numeric values")

    if base <= 0 or height <= 0:
        raise TypeError("Values must be positive")
    return round(0.5 * base * height, 10)

def circle_perimeter(radius_str):
    try:
        radius = float(radius_str)
    except ValueError:
        raise ValueError("Enter numeric values")

    if radius <= 0:
        raise TypeError("Values must be positive")
    return round(2 * math.pi * radius, 10)

def square_perimeter(side_str):
    try:
        side = float(side_str)
    except ValueError:
        raise ValueError("Enter numeric values")

    if side <= 0:
        raise TypeError("Values must be positive")
    return round(4 * side, 10)

def rectangle_perimeter(length_str, width_str):
    try:
        length = float(length_str)
        width = float(width_str)
    except ValueError:
        raise ValueError("Enter numeric values")

    if length <= 0 or width <= 0:
        raise TypeError("Values must be positive")
    return round(2 * (length + width), 10)

def triangle_perimeter(base_str, height_str):
    try:
        base = float(base_str)
        height = float(height_str)
    except ValueError:
        raise ValueError("Enter numeric values")

    if base <= 0 or height <= 0:
        raise TypeError("Values must be positive")
    return round(base + height + math.sqrt(base**2 + height**2), 10)
