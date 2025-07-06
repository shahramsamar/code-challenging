name = input(" Enter a name:")
a,b,c = input(" Enter three numbers:").split()
average = (int(a) + int(b) + int(c)) / 3
print(f"Hello {name}, the average of {a}, {b}, and {c} is {average:.2f}.")