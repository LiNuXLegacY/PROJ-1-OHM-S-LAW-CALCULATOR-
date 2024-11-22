#StartOfTHeProject

def calculate_voltage(current, resistance):
    return current * resistance

def calculate_resistance(voltage, current):
    return voltage / current

def calculate_current(voltage, resistance):
    return voltage / resistance

print("Ohm's Law Calculator")
print("This calculator will help us compute Resistance, Current, and Voltage of an electronic circuit")

print("1. Compute Voltage (V)")
print("2. Compute Resistance (R)")
print("3. Compute Current (I)")

choice = input("Enter choice (1/2/3): ")

if choice == '1':
    current = float(input("Enter current (I): "))
    resistance = float(input("Enter resistance (R): "))
    print("Voltage (V) = ", calculate_voltage(current, resistance))

elif choice == '2':
    voltage = float(input("Enter voltage (V): "))
    current = float(input("Enter current (I): "))
    print("Resistance (R) = ", calculate_resistance(voltage, current))

elif choice == '3':
    voltage = float(input("Enter voltage (V): "))
    resistance = float(input("Enter resistance (R): "))
    print("Current (I) = ", calculate_current(voltage, resistance))

else:
    print("Invalid input")
