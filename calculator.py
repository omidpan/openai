def divide_numbers(a, b):
    """Return the result of dividing ``a`` by ``b``.

    Raises ``ZeroDivisionError`` if ``b`` is zero.
    """
    return a / b

def main():
    print("Welcome to the calculator")
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return

    try:
        result = divide_numbers(num1, num2)
    except ZeroDivisionError:
        print("Cannot divide by zero.")
        return
    print("The result is:", result)

if __name__ == "__main__":
    main()
