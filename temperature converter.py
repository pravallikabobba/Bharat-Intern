import tkinter as tk

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

class TemperatureConverterApp:
    def __init__(self, root):
        self.root = root
        root.title("Temperature Converter")

        # Create input field
        self.input_label = tk.Label(root, text="Enter temperature:")
        self.input_label.pack()

        self.input_entry = tk.Entry(root)
        self.input_entry.pack()

        # Create conversion buttons
        self.c_to_f_button = tk.Button(root, text="Convert to Fahrenheit", command=self.convert_to_fahrenheit)
        self.f_to_c_button = tk.Button(root, text="Convert to Celsius", command=self.convert_to_celsius)

        self.c_to_f_button.pack()
        self.f_to_c_button.pack()

        # Result label
        self.result_label = tk.Label(root, text="")
        self.result_label.pack()

    def convert_to_fahrenheit(self):
        try:
            celsius = float(self.input_entry.get())
            fahrenheit = celsius_to_fahrenheit(celsius)
            self.result_label.config(text=f"{celsius}°C is {fahrenheit:.2f}°F")
        except ValueError:
            self.result_label.config(text="Invalid input. Please enter a number.")

    def convert_to_celsius(self):
        try:
            fahrenheit = float(self.input_entry.get())
            celsius = fahrenheit_to_celsius(fahrenheit)
            self.result_label.config(text=f"{fahrenheit}°F is {celsius:.2f}°C")
        except ValueError:
            self.result_label.config(text="Invalid input. Please enter a number.")

if __name__ == '__main__':
    root = tk.Tk()
    app = TemperatureConverterApp(root)
    root.mainloop()
