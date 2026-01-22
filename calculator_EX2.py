operator = input("Enter your choice (+,-,*,/)")

num1=float(input("enter your no"))
num2=float(input("enter your no"))

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2

print(f"the result is {result}")