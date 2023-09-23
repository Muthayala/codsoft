def add(r, k):
    return r + k

def subtract(r, k):
    return r - k

def multiply(r, k):
    return r * k

def divide(r, k):
    if k == 0:
        return "Cannot divide by zero"
    return r / k

def calculator():
    print("Welcome to the simple calculator!")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    choice = input("Enter choice (1/2/3/4): ")

    if choice in ['1', '2', '3', '4']:
        if choice == '1':
            result = add(num1, num2)
            print("Result:", result)
        elif choice == '2':
            result = subtract(num1, num2)
            print("Result:", result)
        elif choice == '3':
            result = multiply(num1, num2)
            print("Result:", result)
        elif choice == '4':
            result = divide(num1, num2)
            print("Result:", result)
    else:
        print("Invalid input. Please choose a valid operation.")

if __name__ == "__main__":
    calculator()
