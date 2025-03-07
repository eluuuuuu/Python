def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    if num2 == 0:
        return "Error: Division by zero is undefined"
    return num1 / num2

num1 = int(input("Hi, input first number: "))
num2 = int(input("Input your second number: "))
operator = input("Pick an operator (+, -, *, /): ")

if operator == "+":
    result = add(num1, num2)
elif operator == "-":
    result = subtract(num1, num2)
elif operator == "*":
    result = multiply(num1, num2)
elif operator == "/":
    result = divide(num1, num2)
else:
    result = "Invalid operator. Please use +, -, *, or /."

print(f"Result: {result}")
