import random

nums = input("nums: ").split()

for i in range(len(nums)):
    nums[i] = int(nums[i])

n = int(input("shift: "))

n = n % len(nums)

print(nums[-n:] + nums[:-n])

size = int(input("\nsize: "))

list1 = []
list2 = []

for i in range(size):
    list1.append(random.randint(1, 20))
    list2.append(random.randint(1, 20))

print("list1:", list1)
print("list2:", list2)

print("both:", list1 + list2)

print("no dup:", list(set(list1 + list2)))

print("common:", list(set(list1) & set(list2)))

print("unique:", list(set(list1) ^ set(list2)))

print("min max:", min(list1), max(list1), min(list2), max(list2))
