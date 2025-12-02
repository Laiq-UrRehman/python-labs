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
        return "Invalid"

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
sign = input("Enter operation (+, -, *, /): ")

result = calculator(num1, num2, sign)
print("Result:", result)
