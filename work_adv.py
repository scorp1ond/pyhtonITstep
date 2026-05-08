import random


# Завдання 1
def power(a, n):
    if n == 0:
        return 1
    return a * power(a, n - 1)

print(power(2, 3))


# Завдання 2
def is_leap(y):
    return (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0)


def days(m, y):
    d = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if m == 2 and is_leap(y):
        return 29
    return d[m - 1]


def to_days(d, m, y):
    total = 0

    for i in range(1, y):
        total += 365
        if is_leap(i):
            total += 1

    for i in range(1, m):
        total += days(i, y)

    total += d
    return total


def diff(d1, m1, y1, d2, m2, y2):
    return abs(to_days(d1, m1, y1) - to_days(d2, m2, y2))

print(diff(1, 1, 2020, 10, 1, 2020))


# Завдання 3
def min_pos(arr, i=0):
    if i > len(arr) - 10:
        return 0

    s1 = sum(arr[i:i+10])
    s2 = sum(arr[min_pos(arr, i+1):min_pos(arr, i+1)+10])

    if s1 < s2:
        return i
    return min_pos(arr, i+1)


nums = [random.randint(1, 50) for _ in range(100)]
print(min_pos(nums))