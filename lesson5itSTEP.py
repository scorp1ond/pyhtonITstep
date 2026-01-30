# print("For: ")
# for i in range(3):
#     print(i)
#     for j in range(5):
#         print(j, end=' ')
#     print()

# print("While: ")
# counter_outer = 0
# while counter_outer < 3:
#     print(counter_outer)
#     counter_inner = 0
#     while counter_inner < 5:
#         print(counter_inner, end=' ')
#         counter_inner += 1
#     print()
#     counter_outer += 1

import random

# task 1
num = int(input("enter a number for multiplication table: "))
for i in range(1, 11):
    print(num, "x", i, "=", num * i)

print()

# task 2
for i in range(1, 10):
    print("multiplication table for", i)
    for j in range(1, 11):
        print(i, "x", j, "=", i * j)
    print()

# task 3
n = int(input("how many numbers do you want to enter? "))
max_number = None

for i in range(n):
    value = int(input("enter a number: "))
    if max_number is None or value > max_number:
        max_number = value

print("the biggest number is:", max_number)

print()

# task 4
secret = random.randint(1, 500)
tries = 0

while True:
    guess = int(input("guess the number from 1 to 500 (0 to exit): "))

    if guess == 0:
        print("game ended")
        break

    tries += 1

    if guess < secret:
        print("the secret number is bigger")
    elif guess > secret:
        print("the secret number is smaller")
    else:
        print("you guessed the number!")
        print("number of tries:", tries)
        break

print()

# task 5
shape = input("choose a shape (square / rectangle): ")
symbol = input("enter a symbol: ")

if shape == "square":
    side = int(input("enter side length: "))
    for i in range(side):
        print(symbol * side)

elif shape == "rectangle":
    width = int(input("enter width: "))
    height = int(input("enter height: "))
    for i in range(height):
        print(symbol * width)

else:
    print("unknown shape")
