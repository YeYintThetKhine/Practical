finished = False
result = 0
while not finished:
    try:
        number = int(input("Enter integer:"))
        finished = True
        pass
    except ValueError:
        print("Please enter a valid integer.")
print("Valid result is:", result)