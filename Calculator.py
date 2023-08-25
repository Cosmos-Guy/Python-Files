operator = input("Enter An Operator (+ - * / % // **): ")
num1 = float(input("Enter The 1st Number: "))
num2 = float(input("Enter The 2nd Number: "))
result = 0

if operator == "+":
    result = num1 + num2
    print("Your Answer Is: ", round(result, 3))
elif operator == "-":
    result = num1 - num2
    print("Your Answer Is: ", round(result, 3))
elif operator == "*":
    result = num1 * num2
    print("Your Answer Is: ", round(result, 3))
elif operator == "/":
    result = num1 / num2
    print("Your Answer Is: ", round(result, 3))
elif operator == "//":
    result = num1 // num2
    print("Your Answer Is: ", round(result, 3))
elif operator == "**":
    result = num1 ** num2
    print("Your Answer Is: ", round(result, 3))
elif operator == "%":
    result = num1 % num2
    print("Your Answer Is: ", round(result, 3))
else:
    print("Invalid Operator!")