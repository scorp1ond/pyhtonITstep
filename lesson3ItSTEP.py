'''a = int(input('enter a whole number: '))

# short form if
if a % 2 == 0: print(f" number {a} is even") 

# short form if + else
print(f" number {a} is even") if a % 2 == 0 else print(f" number {a} is odd")

day = int(input("enter the day num: "))
match day:
    case 1: print("monday")
    case 2: print("tuesday")
    case 3: print("wednesday")
    case 4: print("thursday")
    case 5: print("friday")
    case 6: print("saturday")
    case 7: print("sunday")
    case _: print("wrong day num")


month = int(input("enter month number"))

match month:
    case 12 | 1 | 2: print("winter")
    case 3 | 4 | 5: print("spring")
    case 6 | 7 | 8: print("summer")
    case 9 | 10 | 11: print("fall")
    case _: print("wrong month num") 

num1 = float(input("enter the first num"))
num2 = float(input("enter second num"))
op = input("enter operation (+, -, *, /, %, //, **): ")
match op:
    case "+": print(f"{num1} + {num2} = {num1 + num2}")
    case "-": print(f"{num1} - {num2} = {num1 - num2}")
    case "*": print(f"{num1} * {num2} = {num1 * num2}")
    case "+": print(f"{num1} + {num2} = {num1 + num2}")
    case "+": print(f"{num1} + {num2} = {num1 + num2}")
    case "+": print(f"{num1} + {num2} = {num1 + num2}")'''



score = int(input("Enter exam score (0-100): "))

if score < 0 or score > 100:
    print("Error")
elif score >= 90:
    print("Excellent")
elif score >= 70:
    print("Good")
elif score >= 50:
    print("Satisfactory")
else:
    print("Unsatisfactory")



salary = float(input("\nEnter salary: "))
years = float(input("Enter years of experience: "))

if years < 1:
    print("No bonus")
elif years < 3:
    print(f"Bonus: {salary * 0.05}")
elif years < 5:
    print(f"Bonus: {salary * 0.10}")
else:
    print(f"Bonus: {salary * 0.15}")



number = int(input("\nEnter a four-digit number: "))
n = abs(number)

if 1000 <= n <= 9999:
    a = n // 1000
    b = n // 100 % 10
    c = n // 10 % 10
    d = n % 10

    s = a + b + c + d

    if s % 2 == 0:
        print("Sum of digits is even")
    else:
        print("Sum of digits is odd")
else:
    print("Error")



number = int(input("\nEnter a six-digit number: "))
n = abs(number)

if 100000 <= n <= 999999:
    a = n // 100000
    b = n // 10000 % 10
    c = n // 1000 % 10
    d = n // 100 % 10
    e = n // 10 % 10
    f = n % 10

    if a + b + c == d + e + f:
        print("Lucky number")
    else:
        print("Not a lucky number")
else:
    print("Error")



number = int(input("\nEnter a six-digit number: "))
n = abs(number)

if 100000 <= n <= 999999:
    a = n // 100000
    b = n // 10000 % 10
    c = n // 1000 % 10
    d = n // 100 % 10
    e = n // 10 % 10
    f = n % 10

    result = f*100000 + e*10000 + c*1000 + d*100 + b*10 + a
    print(f"Result: {result}")
else:
    print("Error")
