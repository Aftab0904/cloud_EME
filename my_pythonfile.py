# cloud_EME
#cloud_eme
#this is python project file
# calculator.py

def main():
    print("Welcome to the Simple Calculator!")
    
    
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /): ")
    
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error! Division by zero."
    else:
        result = "Invalid operation!"
    
    print(f"The result is: {result}")

if __name__ == "__main__":
    main()