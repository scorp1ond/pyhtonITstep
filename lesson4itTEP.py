# while True:
#     num1 = float(input("enter first num: "))
#     num2 = float(input("enter second num: "))
#     op = input('choose and operation  (+ - * /): ')
#     match op:
#         case "+":
#             print(num1 + num2)
#         case "-":
#             print(num1 - num2)
#         case "*":
#             print(num1 * num2)
#         case "/":
#             if num2 == 0:
#                 print("ERROR")
#             else:
#                 print(num1 + num2)
#         case _:
#             print("wrong operation")
#     q = input('enter "q" to exit,=. press enter to continue. ')
#     if q == 'q':
#         break
# Task 1
# Task 1
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

start = min(a, b)
end = max(a, b)

i = start
while i <= end:
    print(i)
    i += 1

# Task 2
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

start = min(a, b)
end = max(a, b)

i = start
while i <= end:
    if i % 2 != 0:
        print(i)
    i += 1

# Task 3
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

start = min(a, b)
end = max(a, b)

i = end
while i >= start:
    if i % 2 == 0:
        print(i)
    i -= 1

# Task 4
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
order = int(input("Enter order (1 = ascending, 2 = descending): "))

start = min(a, b)
end = max(a, b)

if order == 1:
    i = start
    while i <= end:
        print(i)
        i += 1
elif order == 2:
    i = end
    while i >= start:
        print(i)
        i -= 1

# Task 5
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

start = min(a, b)
end = max(a, b)

i = start
while i <= end:
    if i % 2 != 0:
        print(i)
    i += 1

# Task 6
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

start = min(a, b)
end = max(a, b)

i = start
while i <= end:
    if i % 2 == 0:
        print(i)
    i += 1

i = end
while i >= start:
    if i % 2 != 0:
        print(i)
    i -= 1

