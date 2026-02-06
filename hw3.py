number = int(input("Enter number: "))
power = int(input("Enter power (0-7): "))

if power < 0 or power > 7:
    print("Error. Power must be from 0 to 7")
else:
    result = 1
    for i in range(power):
        result *= number
    print("Result:", result)

n = int(input("Enter number (1-100): "))

if n < 1 or n > 100:
    print("Error. Number out of range")
elif n % 3 == 0 and n % 5 == 0:
    print("Fizz Buzz")
elif n % 3 == 0:
    print("Fizz")
elif n % 5 == 0:
    print("Buzz")
else:
    print(n)

total = 0
discount = 0

print("Starters: 1-Salad 2-Soup")
starter = int(input())

print("Main dishes: 1-Chicken 2-Fish")
main_dish = int(input())

print("Desserts: 1-Ice cream 2-Fruits")
dessert = int(input())

regular = int(input("Regular client? 1-Yes 0-No: "))

if starter == 1:
    total += 5
elif starter == 2:
    total += 7

if main_dish == 1:
    total += 10
elif main_dish == 2:
    total += 12

if dessert == 1:
    total += 3
elif dessert == 2:
    total += 4

if starter and main_dish and dessert:
    discount = 0.10

if total > 20:
    discount = 0.15

if regular == 1:
    discount += 0.05

if starter == 2 and main_dish == 2:
    total -= 2

free_drink = False
if main_dish == 1 and dessert == 1:
    free_drink = True

total = total - total * discount

print("Total price:", total)

if free_drink:
    print("Bonus: Free tea")
