num1 = int(input("number1: "))
num2 = int(input("number2: "))
num3 = int(input("number3: "))

if num1 + num2 > num3 and num1 + num3 > num2 and num2 + num3 > num1:
    print("Yes")
else:
    print("No")