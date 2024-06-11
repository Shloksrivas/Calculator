#CALCULATOR

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y

def main():
    print("Simple Calculator")
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    
    while True:
        try:
            choice = input("Enter your choice (1-4): ")
            if choice not in ['1', '2', '3', '4']:
                print("Invalid selection of operation")
                continue
            
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if choice == '1':
                print(f"The result is: {add(num1, num2)}")
            elif choice == '2':
                print(f"The result is: {subtract(num1, num2)}")
            elif choice == '3':
                print(f"The result is: {multiply(num1, num2)}")
            elif choice == '4':
                try:
                    print(f"The result is: {divide(num1, num2)}")
                except ValueError as e:
                    print(e)

            next_operation = input("Do you want to perform another calculation? (yes/no): ")
            if next_operation.lower() != 'yes':
                break

        except ValueError:
            print("Invalid input, please enter numeric values.")

if __name__ == "__main__":
    main()
