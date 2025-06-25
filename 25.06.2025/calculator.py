a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operator (+ - * /): ")

if op == '+':
    print(a + b)
elif op == '-':
    print(a - b)
elif op == '*':
    print(a * b)
elif op == '/':
    print(a / b if b != 0 else "Divide by zero error")
else:
    print("Invalid operator")
