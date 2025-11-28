number = [34, 1, 78, 12, 45, 99, 23]

first_max = 0
second_max = 0

for num in number:
    if num > first_max:
        second_max = first_max
        first_max = num
    elif num > second_max and num != first_max:
        second_max = num

print(f" Second maximum number: {second_max}")
