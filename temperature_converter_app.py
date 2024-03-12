from temperature_converter import TemperatureConverter

class TemperatureConverterApp:
    def __init__(self):
        self.converter = TemperatureConverter()

    def display_menu(self):
        print("\nTemperature Converter Menu:")
        print("1. Convert Celsius to Fahrenheit")
        print("2. Convert Fahrenheit to Celsius")
        print("3. Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")

            if choice == "1":
                self.celsius_to_fahrenheit()
            elif choice == "2":
                self.fahrenheit_to_celsius()
            elif choice == "3":
                print("Exiting Temperature Converter.")
                break
            else:
                print("Invalid choice. Please try again.")

    def celsius_to_fahrenheit(self):
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = self.converter.celsius_to_fahrenheit(celsius)
        print(f"{celsius}°C is equal to {fahrenheit:.2f}°F")

    def fahrenheit_to_celsius(self):
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = self.converter.fahrenheit_to_celsius(fahrenheit)
        print(f"{fahrenheit}°F is equal to {celsius:.2f}°C")

if __name__ == "__main__":
    app = TemperatureConverterApp()
    app.run()
