num = int(input("Enter a number: "))

count_digits = 0


for digit in str(num):
    count_digits += int(digit)

print(f"sum: {num} equal: {count_digits}.")