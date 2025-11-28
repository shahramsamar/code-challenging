numbers = [34, 1, 78, 12, 45, 99, 23]
threshold = 40

count_smaller = sum(1 for number in numbers if number < threshold)
print(f"Count of numbers  smaller than {threshold}: {count_smaller}")