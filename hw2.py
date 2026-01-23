day = int(input("Enter day number (1-7): "))

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid day number")

month = int(input("Enter month number (1-12): "))

match month:
    case 1:
        print("January")
    case 2:
        print("February")
    case 3:
        print("March")
    case 4:
        print("April")
    case 5:
        print("May")
    case 6:
        print("June")
    case 7:
        print("July")
    case 8:
        print("August")
    case 9:
        print("September")
    case 10:
        print("October")
    case 11:
        print("November")
    case 12:
        print("December")
    case _:
        print("Invalid month number")

price = float(input("Enter purchase amount: "))
age = int(input("Enter your age: "))

match age:
    case _ if age < 18:
        discount = 0.10
    case _ if age <= 60:
        discount = 0.05
    case _:
        discount = 0.15

print("Final price:", price - price * discount)

g1 = int(input("Grade 1: "))
g2 = int(input("Grade 2: "))
g3 = int(input("Grade 3: "))

match (g1, g2, g3):
    case _ if 2 in (g1, g2, g3):
        print("Unsatisfactory")
    case _ if g1 >= 4 and g2 >= 4 and g3 >= 4:
        print("Excellent")

g1 = int(input("Grade 1: "))
g2 = int(input("Grade 2: "))
g3 = int(input("Grade 3: "))
g4 = int(input("Grade 4: "))

grades = (g1, g2, g3, g4)

match grades:
    case _ if any(g < 3 for g in grades):
        print("Student is NOT admitted to the exam")
    case _ if all(g >= 4 for g in grades):
        print("Student is admitted to the exam with honors")
    case _:
        print("Student is admitted to the exam")

car_age = int(input("Car age (years): "))
mileage = int(input("Mileage (km): "))

match (car_age, mileage):
    case _ if car_age < 3 and mileage <= 30000:
        print("Car is in excellent condition")
    case _ if car_age <= 10 and mileage <= 100000:
        print("Car is in good condition")
    case _:
        print("Car needs inspection")
