text = "hello welcome to the world of python"
sub = input("enter your word: ")
if sub in text:
    print(f"substring  {sub} is found")
else:
    print(f"substring {sub} isn't found")