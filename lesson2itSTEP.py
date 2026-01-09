#task 1
num = int(input("enter number:"))
if num %2 == 0:
    print("even number")
else:
    print("odd number")

#task 2

num = int(input("enter number: "))
if num % 7 == 0:
    print("Number is multiple 7")
else:
    print("Number is not multiple 7")

#task 3

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

if a > b:
    print(f"The largest number is: {a}")
else:
    print(f"The largest number is: {b}")

#task 4

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

if a < b:
    print(f"The smallest number is: {a}")
else:
    print(f"The smallest number is: {b}")

#task 5

usd = float(input("Enter amount in dollars (USD): "))
currency = input("Choose currency (EUR, GBP, UAH): ")

if currency == "EUR" or currency == "GBP" or currency == "UAH":
    rate = float(input("Enter exchange rate to USD: "))
    converted = usd * rate
    print(f"Converted amount: {converted}{currency}")
else:
    print("Invalid currency choice")

#task 6


seconds_passed = int(input("Enter seconds passed since start of the day: "))

seconds_in_day = 24 * 60 * 60
seconds_left = seconds_in_day - seconds_passed

hours = seconds_left // 3600
minutes = (seconds_left % 3600) // 60
seconds = seconds_left % 60

print(f"Time left until midnight: {hours} hours {minutes} minutes {seconds} seconds")


#task 7


diameter = float(input("Enter the diameter of the circle: "))
choice = input("Choose what to calculate (area / perimeter): ")

radius = diameter / 2
pi = 3.14

match choice:
    case "area":
        area = pi * radius * radius
        print(f"Area of the circle: {area}")
    case "perimeter":
        perimeter = 2 * pi * radius
        print(f"Perimeter of the circle: {perimeter}")
    case _:
        print(f"Invalid choice")

'''
num1 = float(input("enter first num: "))
num2 = float(input("enter second num: "))
operation = input("enter operation(+ - * /): ")

match operation:
    case '+':
        print(f"{num1} + {num2} = {num1 + num2}")
    case '-':
        print(f"{num1} - {num2} = {num1 - num2}")
    case '*':
        print(f"{num1} * {num2} = {num1 * num2}")
    case '/':
        if num2 == 0:
            print("you cant devide by 0")
        else:
            print(f"{num1} / {num2} = {num1 / num2}")


if operation == "+":
    print(f"{num1} + {num2} = {num1 + num2}")
elif operation == "-":
    print(f"{num1} - {num2} = {num1 - num2}")
elif operation == "*":
    print(f"{num1} * {num2} = {num1 * num2}")
elif operation == "/":
    if num2 == 0:
        print("you cant devide by 0")
    else:
        print(f"{num1} / {num2} = {num1 / num2}")
else:
    print("unknown operator")
num = int(input("enter a whole number:"))

if num >= 10 and num <= 20:
    print(f"{num} is in the range of 10 between 20")
else:
    print(f"{num} is not in the range of 10 between 20")


can_penguins_swim = True
can_penguins_fly = False
PI = 3.14

print(f"penguins can swim: {can_penguins_swim}")
print(f"penguins can fly: {can_penguins_fly}")
print(type(can_penguins_fly))
print(type(can_penguins_swim))

number = int(input("enter a whole number: "))

print(f"{number} > 10? {number > 10}")
print(f"{number} < 10? {number < 10}")
print(f"{number} >= 10? {number >= 10}")
print(f"{number} <= 10? {number <= 10}")
print(f"{number} == 10? {number == 10}")
print(f"{number} != 10? {number > 10}") 

print(f"True and True = {True and True}")
print(f"False and True = {False and True}")
print(f"True and False = {True and False}")
print(f"False and False = {False and False}")

print(f"True or True = {True or True}")
print(f"False or True = {False or True}")
print(f"True or False = {True or False}")
print(f"False or False = {False or False}")

print(f"not True = {not True}")
print(f"not False = {not False}")



temp = int(input("whats thr temp today: "))

if temp <= 0:
    print("wear a  winter jacket")
    print("wear a hat")
    print("wear a gloves")

elif temp > 0 and temp < 15:
    print("wear a hoodie")
    print("wear a hat")

else:
    print("whear a tshirt")
    print("wear a cap")

print("go outside")

'''