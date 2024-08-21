while True:
    try:
        number1 = int(input("Please enter number 1: "))
        number2 = int(input("Please enter number 2: "))
        result = number1 / number2
        print("Result: " + str(result))
    except ValueError:
        print("Please enter a valid number.")
    except ZeroDivisionError:
        print("Division by zero is not allowed.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    
    print("---")
