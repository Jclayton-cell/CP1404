finished = False
result = 0

while not finished:
    try:
        result = int(input("Enter a Valid Int: "))
        finished = True
    except ValueError:
        print("Please enter a valid Int.")
print("Valid result is:", result)
