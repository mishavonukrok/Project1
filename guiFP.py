import tkinter as tk
from tkinter import *
import calculator

class GUI:
    def __init__(self, window):
        self.window = window

        # Radio buttons for shape
        self.frame_shape = Frame(self.window)
        self.label_operation = Label(self.frame_shape, text='Shape\t')
        self.radio_1 = IntVar()
        self.radio_1.set(0)
        self.radio_circle = Radiobutton(self.frame_shape, text='Circle', variable=self.radio_1, value=1, command=self.shape)
        self.radio_square = Radiobutton(self.frame_shape, text='Square', variable=self.radio_1, value=2, command=self.shape)
        self.radio_rectangle = Radiobutton(self.frame_shape, text='Rectangle', variable=self.radio_1, value=3, command=self.shape)
        self.radio_triangle = Radiobutton(self.frame_shape, text='Triangle', variable=self.radio_1, value=4, command=self.shape)
        self.label_operation.pack(side='left', padx=5)
        self.radio_circle.pack(side='left')
        self.radio_square.pack(side='left')
        self.radio_rectangle.pack(side='left')
        self.radio_triangle.pack(side='left')
        self.frame_shape.pack(anchor='w', pady=10)

        # Radio buttons for operation
        self.frame_operation = Frame(self.window)
        self.label_operation = Label(self.frame_operation, text='Operation\t')
        self.radio_2 = IntVar()
        self.radio_2.set(0)
        self.radio_area = Radiobutton(self.frame_operation, text='Area', variable=self.radio_2, value=1, command=self.operation)
        self.radio_perimeter = Radiobutton(self.frame_operation, text='Perimeter', variable=self.radio_2, value=2, command=self.operation)
        self.label_operation.pack(side='left', padx=5)
        self.radio_area.pack(side='left')
        self.radio_perimeter.pack(side='left')
        self.frame_operation.pack(anchor='w', pady=10)

        # First number
        self.frame_first = Frame(self.window)
        self.label_first = Label(self.frame_first)
        self.entry_first = Entry(self.frame_first, width=40)
        self.label_first.pack(padx=20, side='left')
        self.entry_first.pack(padx=20, side='left')
        self.frame_first.pack(anchor='w', pady=10)
        self.entry_first.pack_forget()

        # Second number
        self.frame_second = Frame(self.window)
        self.label_second = Label(self.frame_second)
        self.entry_second = Entry(self.frame_second, width=40)
        self.label_second.pack(padx=20, side='left')
        self.entry_second.pack(padx=20, side='left')
        self.frame_second.pack(anchor='w', pady=10)
        self.entry_second.pack_forget()

        # Results label
        self.frame_result = Frame(self.window)
        self.label_result = Label(self.frame_result)
        self.label_result.pack(pady=10)
        self.frame_result.pack()

        # Create a canvas for drawing shapes
        self.canvas = Canvas(self.window, width=600, height=300, bg="black")
        self.canvas.pack(pady=10)
        
        # Compute button
        self.frame_button = Frame(self.window)
        self.button_compute = Button(self.frame_button, text='COMPUTE', command=self.compute_area)
        self.button_compute.pack(pady=10)
        self.frame_button.pack()

    def shape(self):
        """Handles shape selection, updates the labels and input fields."""
        self.entry_first.delete(0, END)
        self.entry_second.delete(0, END)
        self.label_result.config(text='')
        self.entry_first.pack()
        shape = self.radio_1.get()

        if shape == 1:
            self.label_first.config(text='Radius')
            self.label_second.config(text='')
            self.entry_second.pack_forget()
        elif shape == 2:
            self.label_first.config(text='Side')
            self.label_second.config(text='')
            self.entry_second.pack_forget()
        elif shape == 3:
            self.label_first.config(text='Length')
            self.label_second.config(text='Width')
            self.entry_second.pack()
        elif shape == 4:
            self.label_first.config(text='Base')
            self.label_second.config(text='Height')
            self.entry_second.pack()

    def operation(self):
        """Updates the compute button command based on the selected operation."""
        operation = self.radio_2.get()

        if operation == 1:
            self.button_compute.config(text='COMPUTE AREA', command=self.compute_area)
        elif operation == 2:
            self.button_compute.config(text='COMPUTE PERIMETER', command=self.compute_perimeter)
        else:
            self.button_compute.config(text='COMPUTE', command=lambda: None)

    def compute_area(self):
        """Calculates the area and draws the shape based on user input."""
        try:
            first_num = float(self.entry_first.get())
            second_num = float(self.entry_second.get()) if self.entry_second.winfo_viewable() else 0.0
            shape = self.radio_1.get()

            self.canvas.delete("all")

            if shape == 1:
                self.label_result.config(text=f'Circle area = {calculator.circle_area(first_num)}')
                self.draw_circle(first_num)
            elif shape == 2:
                self.label_result.config(text=f'Square area = {calculator.square_area(first_num)}')
                self.draw_square(first_num)
            elif shape == 3:
                self.label_result.config(text=f'Rectangle area = {calculator.rectangle_area(first_num, second_num)}')
                self.draw_rectangle(first_num, second_num)
            elif shape == 4:
                self.label_result.config(text=f'Triangle area = {calculator.triangle_area(first_num, second_num)}')
                self.draw_triangle(first_num, second_num)
            else:
                self.label_result.config(text='No operation selected')
        except ValueError:
            self.label_result.config(text='Enter numeric values')
        except TypeError:
            self.label_result.config(text='Values must be positive')

    def compute_perimeter(self):
        """Calculates the perimeter and draws the shape based on user input."""
        try:
            first_num = float(self.entry_first.get())
            second_num = float(self.entry_second.get()) if self.entry_second.winfo_viewable() else 0.0
            shape = self.radio_1.get()

            self.canvas.delete("all")

            if shape == 1:
                self.label_result.config(text=f'Circle perimeter = {calculator.circle_perimeter(first_num)}')
                self.draw_circle(first_num)
            elif shape == 2:
                self.label_result.config(text=f'Square perimeter = {calculator.square_perimeter(first_num)}')
                self.draw_square(first_num)
            elif shape == 3:
                self.label_result.config(text=f'Rectangle perimeter = {calculator.rectangle_perimeter(first_num, second_num)}')
                self.draw_rectangle(first_num, second_num)
            elif shape == 4:
                self.label_result.config(text=f'Triangle perimeter = {calculator.triangle_perimeter(first_num, second_num)}')
                self.draw_triangle(first_num, second_num)
            else:
                self.label_result.config(text='No operation selected')
        except ValueError:
            self.label_result.config(text='Enter numeric values')
        except TypeError:
            self.label_result.config(text='Values must be positive')

    def draw_circle(self, radius):
        """Draws a circle with the given radius."""
        center_x, center_y = 300, 150
        radius = float(radius)
        scaled_radius = 100

        self.canvas.create_oval(center_x - scaled_radius, center_y - scaled_radius,
                                center_x + scaled_radius, center_y + scaled_radius,
                                fill="red", outline="white", width=1)

        self.canvas.create_line(center_x, center_y, center_x + scaled_radius, center_y, fill="white", width=1)
        self.canvas.create_text(center_x + scaled_radius / 2, center_y - 20, text=f"{radius}", font=("Arial", 12))
        self.canvas.create_text(450, 75, text="A = π × r²", font=("Arial", 15))
        self.canvas.create_text(450, 125, text="P = 2πr", font=("Arial", 15))


    def draw_square(self, side):
        """Draws a square with a given side."""
        center_x, center_y = 300, 150
        side = float(side)
        scaled_side = 200
        self.canvas.create_rectangle(center_x - scaled_side / 2, center_y - scaled_side / 2, center_x + scaled_side / 2, center_y + scaled_side / 2, fill="red")
        self.canvas.create_text(center_x - scaled_side / 2 - 20, center_y, text=f"{side}", font=("Arial", 12))
        self.canvas.create_text(450, 75, text="A = s²", font=("Arial", 15))
        self.canvas.create_text(450, 125, text="P = 4s", font=("Arial", 15))


    def draw_rectangle(self, length, width):
        """Draws a rectangle with given length and width."""
        center_x, center_y = 300, 150
        length, width = float(length), float(width)
        ratio = width / length
        scaled_length, scaled_width = 200, int(200 * ratio)
        if width > length:
            scaled_length, scaled_width = min(100, scaled_width), min(200, scaled_length)
        self.canvas.create_rectangle(center_x - scaled_length / 2, center_y - scaled_width / 2, center_x + scaled_length / 2, center_y + scaled_width / 2, fill="red")
        self.canvas.create_text(center_x - scaled_length / 2 - 20, center_y, text=f"{width}", font=("Arial", 12))
        self.canvas.create_text(center_x, center_y - scaled_width / 2 - 20, text=f"{length}", font=("Arial", 12))
        self.canvas.create_text(450, 75, text="A = L × W", font=("Arial", 15))
        self.canvas.create_text(450, 125, text="P = 2L + 2W", font=("Arial", 15))
        
    def draw_triangle(self, base, height):
        """Draws a right-angled triangle with given base and height."""
        center_x, center_y = 300, 150
        base, height = float(base), float(height)
        scaled_base, scaled_height = 200, 100

        if height > base:
            scaled_base, scaled_height = min(100, scaled_base), min(200, scaled_height)

        self.canvas.create_polygon(
            center_x - scaled_base / 2, center_y + scaled_height / 2,
            center_x - scaled_base / 2, center_y - scaled_height / 2,
            center_x + scaled_base / 2, center_y + scaled_height / 2,
            fill="red", outline="white", width = 1
        )

        self.canvas.create_text(center_x - scaled_base / 2 - 20, center_y, text=f"{height}", font=("Arial", 12))
        self.canvas.create_text(center_x, center_y + scaled_height / 2 + 20, text=f"{base}", font=("Arial", 12))
        self.canvas.create_text(450, 75, text="A = ½ × B × H", font=("Arial", 15))
        self.canvas.create_text(450, 100, text="P = B + H + √(B² + H²)", font=("Arial", 15))