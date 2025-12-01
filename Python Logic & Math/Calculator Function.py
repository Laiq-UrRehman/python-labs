def calculator(n1, n2, op):
    if op == "+":
        return n1 + n2
    elif op == "-":
        return n1 - n2
    elif op == "*":
        return n1 * n2
    elif op == "/":
        return n1 / n2
    else:
        return "Wrong operator"

# Get simple input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
symbol = input("Enter operation (+, -, *, /): ")

# Call function
print("The result is:", calculator(num1, num2, symbol))