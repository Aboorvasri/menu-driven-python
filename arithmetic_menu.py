def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b

def power(a, b):
    return a ** b

def modulus(a, b):
    return a % b



history = []
count = 0
limit = 10  

while True:
    print("\n--- MENU ---")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Modulus")
    print("7. View History")
    print("8. Exit")

    choice = input("Enter your choice (1-8): ")

   
    if choice == '8':
        confirm = input("Are you sure you want to exit? (y/n): ")
        if confirm.lower() == 'y':
            print("Exiting program...")
            break
        else:
            continue

    
    if choice == '7':
        if history:
            print("\n--- Calculation History ---")
            for item in history:
                print(item)
        else:
            print("No history yet.")
        continue

    if choice in ['1', '2', '3', '4', '5', '6']:
        try:
            num1 = float(input("Enter first number (0–100): "))
            num2 = float(input("Enter second number (0–100): "))

            
            if not (0 <= num1 <= 100 and 0 <= num2 <= 100):
                print("Please enter numbers between 0 and 100 only.")
                continue

            
            count += 1
            if count > limit:
                print("Operation limit reached!")
                break

            
            if choice == '1':
                result = add(num1, num2)
                expression = f"{num1} + {num2} = {result}"

            elif choice == '2':
                result = subtract(num1, num2)
                expression = f"{num1} - {num2} = {result}"

            elif choice == '3':
                result = multiply(num1, num2)
                expression = f"{num1} * {num2} = {result}"

            elif choice == '4':
                if abs(num2) < 0.0001:
                    print("Number too small for safe division.")
                    continue
                result = divide(num1, num2)
                expression = f"{num1} / {num2} = {result}"

            elif choice == '5':
                result = power(num1, num2)
                expression = f"{num1} ^ {num2} = {result}"

            elif choice == '6':
                result = modulus(num1, num2)
                expression = f"{num1} % {num2} = {result}"

            print("Result:", result)

            
            history.append(expression)

        except ValueError:
            print("Invalid input! Please enter numbers only.")

    else:
        print("Invalid choice! Please select from 1 to 8.")