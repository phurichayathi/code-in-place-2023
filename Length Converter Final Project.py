"""
Program: Length Converter
--------------------
This program will converter from 
inches to centimeters or centimeters to inches
and prints the value
"""
def main():
    print("Length Converter")
    print("1. inches to centimeters 2. centimeters to inches")
    select = int(input("Type number 1 or 2: "))
    
    # Convert inches to centimeters
    if select == 1:
        inches1 = float(input("Your length inches: "))
        cm1 = round(inches1 * 2.54, 2)
        print(f'{inches1} inches is equal to {cm1} centimeters.')
        
    # Convert centimeters to inches
    elif select == 2:
        cm2 = float(input("Your length centimeters: "))
        inches2 = round(cm2 / 2.54, 2)
        print(f'{cm2} centimeters is equal to {inches2} inches.')
        
    else:
        print("Type number (1) inches to centimeters OR (2) centimeters to inches")

while True:
    main()
    choice = input("Do you want to continue? (y/n): ")

    if choice.lower() != 'y':
        break

if __name__ == "__main__":
    main()
