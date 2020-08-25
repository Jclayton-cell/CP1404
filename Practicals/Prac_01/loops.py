for i in range(1, 21, 2):
    print(i, end=' ')
print()

for x in range(0, 101, 10):
    print(x, end=' ')
print()

for y in range(20, 0, -1):
    print(y, end=' ')
print()

stars = "*"
num_stars = int(input("How many stars would you like?: "))
print(stars * num_stars)
print()

rows = int(input("How many rows of stars: "))
for a in range(0, rows):
    for b in range(0, a + 1):
        print("*", end='')
    print("\r")
