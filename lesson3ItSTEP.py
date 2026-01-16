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
    print("Error: score must be between 0 and 100")
else:
    match score:
        case s if s >= 90:
            print("Excellent")
        case s if s >= 70:
            print("Good")
        case s if s >= 50:
            print("Satisfactory")
        case _:
            print("Unsatisfactory")



salary = float(input("Enter salary: "))
years = float(input("Enter years of experience: "))

match years:
    case y if y < 1:
        print("No bonus")
    case y if 1 <= y < 3:
        bonus = salary * 0.05
        print(f"Bonus: {bonus}")
    case y if 3 <= y < 5:
        bonus = salary * 0.10
        print(f"Bonus: {bonus}")
    case _:
        bonus = salary * 0.15
        print(f"Bonus: {bonus}")




number = int(input("Enter a four-digit number: "))
n = abs(number)

if 1000 <= n <= 9999:
    a = n // 1000
    b = n // 100 % 10
    c = n // 10 % 10
    d = n % 10

    digit_sum = a + b + c + d

    if digit_sum % 2 == 0:
        print("Sum of digits is even")
    else:
        print("Sum of digits is odd")
else:
    print("Error: not a four-digit number")




number = int(input("Enter a six-digit number: "))
number_abs = abs(number)

if 100000 <= number_abs <= 999999:
    digits = list(map(int, str(number_abs)))
    match sum(digits[:3]) == sum(digits[3:]):
        case True:
            print("Lucky number")
        case False:
            print("Not a lucky number")
else:
    print("Error: not a six-digit number")



number = int(input("Enter a six-digit number: "))
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
    print("Error: not a six-digit number")