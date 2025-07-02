def divide_numbers(a, b):
    return a / b

def main():
    print("Welcome to the calculator")
    num1 = input("Enter the first number:")
    num2 = input("Enter the second number:")

    result = divide_numbers(num1, num2)
    print("The result is:", result)

if __name__ == "__main__":
    main()
