num1 = int(input("number 1:"))
num2 = int(input("number 2:"))
sub = num1 - num2
sum = num1 + num2
mul = num1 * num2
div = num1 / num2 if num2 != 0 else "undefined (division by zero)"
print(f"Results for {num1} and {num2}:")
print(f"Subtraction: {num1} - {num2} = {sub}")
print(f"Addition: {num1} + {num2} = {sum}")
print(f"Multiplication: {num1} * {num2} = {mul}")
print(f"Division: {num1} / {num2} = {div}")
