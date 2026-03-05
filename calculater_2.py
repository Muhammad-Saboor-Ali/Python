import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero!"
    return a / b

def power(a, b):
    return a ** b

def square_root(a):
    if a < 0:
        return "Error: Negative number!"
    return math.sqrt(a)

def calculator():
    while True:
        print("\n--- Python Calculator ---")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Power (^)")
        print("6. Square Root (√)")
        print("7. Exit")

        choice = input("Choose an operation (1-7): ")

        if choice == "7":
            print("Exiting calculator. Goodbye!")
            break
        elif choice == "6":
            num = float(input("Enter number: "))
            print("Result:", square_root(num))
        elif choice in ["1","2","3","4","5"]:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == "1":
                print("Result:", add(num1, num2))
            elif choice == "2":
                print("Result:", subtract(num1, num2))
            elif choice == "3":
                print("Result:", multiply(num1, num2))
            elif choice == "4":
                print("Result:", divide(num1, num2))
            elif choice == "5":
                print("Result:", power(num1, num2))
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    calculator()
    