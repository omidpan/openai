def divide_numbers(a, b):
    return a / b

def main():
    print("Welcome to the calculator")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    try:
        result = divide_numbers(num1, num2)
        print("The result is:", result)
    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

if __name__ == "__main__":
    main()
