"""Files"""
OUTPUT_FILE = "name"
INPUT_FILE = "numbers"
output_file = open(OUTPUT_FILE, 'w')

# Write name & read name
name = input("What is your name?: ")
print("Your name is {}".format(name), file=output_file)
output_file.close()
input_file = open(OUTPUT_FILE, 'r')
print(input_file.read())
input_file.close()

#Read numbers and add
input_file2 = open(INPUT_FILE, 'r')
number1 = int(input_file2.readline())
number2 = int(input_file2.readline())
input_file2.close
print((number1 + number2))

#Total
input_file2 = open(INPUT_FILE, "r")
total = 0
for line in input_file2:
    number = int(line)
    total += number
input_file2.close()
print(total)