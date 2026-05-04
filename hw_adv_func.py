def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

a = int(input())
b = int(input())

print(gcd(a, b))

def sum_digits(n):
    if n == 0:
        return 0
    return (n % 10) + sum_digits(n // 10)

n = int(input())

print(sum_digits(n))

def symmetric(lst):
    if len(lst) <= 1:
        return True
    if lst[0] != lst[-1]:
        return False
    return symmetric(lst[1:-1])

lst = input().split()

for i in range(len(lst)):
    lst[i] = int(lst[i])

if symmetric(lst):
    print("yes")
else:
    print("no")