# LEVEL 1 - Task 1
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = float(input("Enter the third number: "))
sum_numbers = a + b + c
product_numbers = a * b * c
print("Sum:", sum_numbers)
print("Product:", product_numbers)

# LEVEL 1 - Task 2
d1 = float(input("Enter the first diagonal: "))
d2 = float(input("Enter the second diagonal: "))
area_rhombus = (d1 * d2) / 2
print("Area of the rhombus:", area_rhombus)

# LEVEL 2 - Task 3
salary = float(input("Enter monthly salary: "))
loan = float(input("Enter loan payment: "))
utilities = float(input("Enter utilities debt: "))
remaining_money = salary - loan - utilities
print("Money left after payments:", remaining_money)

# LEVEL 2 - Task 4
distance = float(input("Enter distance (km): "))
fuel_per_100 = float(input("Enter fuel consumption per 100 km: "))
price_per_liter = float(input("Enter price per liter: "))
fuel_used = distance * fuel_per_100 / 100
trip_cost = fuel_used * price_per_liter
print("Total trip cost:", trip_cost)

# LEVEL 3 - Task 5
bill = float(input("Enter total bill amount: "))
people = int(input("Enter number of people: "))
tip = bill * 0.15
total_with_tip = bill + tip
per_person = total_with_tip / people
print("Tip amount:", tip)
print("Total amount with tip:", total_with_tip)
print("Amount per person:", per_person)

# LEVEL 3 - Task 6
price_per_day = float(input("Enter rental price per day: "))
days = int(input("Enter number of rental days: "))
deposit = float(input("Enter deposit amount: "))
rental_cost = price_per_day * days
total_with_deposit = rental_cost + deposit
payment_after_return = rental_cost
cost_per_day = rental_cost / days
print("Total cost including deposit:", total_with_deposit)
print("Amount to pay after returning the car:", payment_after_return)
print("Rental cost per day:", cost_per_day)

