def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5.0 / 9.0

def celsius_to_fahrenheit(celsius):
    return (celsius * 9.0 / 5.0) + 32

def main():
    while True:
        print("\nTemperature Converter")
        print("1. Convert Fahrenheit to Celsius")
        print("2. Convert Celsius to Fahrenheit")
        print("3. Exit")

        choice = input("\nChoose an option (1/2/3): ")

        if choice == '1':
            while True:
                try:
                    fahrenheit = float(input("\nEnter temperature in Fahrenheit: "))
                    celsius = fahrenheit_to_celsius(fahrenheit)
                    print(f"\nTemperature: {fahrenheit:.1f}F = {celsius:.2f}C")
                    break
                except ValueError:
                    print("⚠ Invalid input! Please enter a valid number.")

        elif choice == '2':
            while True:
                try:
                    celsius = float(input("\nEnter temperature in Celsius: "))
                    fahrenheit = celsius_to_fahrenheit(celsius)
                    print(f"Temperature: {celsius:.1f}C = {fahrenheit:.2f}F")
                    break
                except ValueError:
                    print("⚠ Invalid input! Please enter a valid number.")

        elif choice == '3':
            print("\nThank you. 👋Goodbye!\n")
            break

        else:
            print("\n⚠ Invalid choice! Please enter 1, 2, or 3.")

# Call the main function
if __name__ == '__main__':
    main()
