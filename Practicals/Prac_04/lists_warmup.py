numbers = [3, 1, 4, 1, 5, 9, 2]
# numbers[0] = 3
# numbers[-1] = 2
# numbers[3] = 1
# numbers[:-1] = 3 1 4 5 9
# numbers[3:4] = 1
# 5 in numbers = true
# 7 in numbers
# "3" in numbers = false
# numbers + [6, 5, 3] = 3 1 4 1 5 9 2 6 5 3

# Change the first element of numbers to "ten" (the string, not the number 10)
# Change the last element of numbers to 1
# Get all the elements from numbers except the first two (slice)
# Check if 9 is an element of numbers
numbers[0] = "ten"
numbers[-1] = 1
print(numbers[0])
print(numbers[-1])
print(numbers[2:])
print(9 in numbers)
