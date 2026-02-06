start = int(input())
end = int(input())

i = start
while i <= end:
    if i % 7 == 0:
        print(i)
    i += 1


start = int(input())
end = int(input())

i = start
while i <= end:
    print(i)
    i += 1

i = end
while i >= start:
    print(i)
    i -= 1

i = start
while i <= end:
    if i % 7 == 0:
        print(i)
    i += 1

count = 0
i = start
while i <= end:
    if i % 5 == 0:
        count += 1
    i += 1

print(count)


start = int(input())
end = int(input())

i = start
while i <= end:
    if i % 3 == 0 and i % 5 == 0:
        print("Fizz Buzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
    i += 1


start = int(input())
end = int(input())
step = int(input())
order = int(input())

if order == 1:
    i = start
    while i <= end:
        print(i)
        i += step
else:
    i = end
    while i >= start:
        print(i)
        i -= step


start = int(input())
end = int(input())

if start > end:
    start, end = end, start

product = 1
found = False

i = start
while i <= end:
    if i % 4 == 0 and i % 6 != 0:
        product *= i
        found = True
    i += 1

if found:
    print(product)
else:
    print("No suitable numbers")


a = int(input())
n = int(input())

result = 1
i = 0
while i < n:
    result *= a
    i += 1

print(result)
