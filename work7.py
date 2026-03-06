import random

nums = list(map(int, input("Enter integers separated by space: ").split()))
n = int(input("Enter shift N: "))

n = n % len(nums)
shifted = nums[-n:] + nums[:-n]

print("Shifted list:", shifted)


size = int(input("\nEnter list size: "))

list1 = [random.randint(1, 20) for _ in range(size)]
list2 = [random.randint(1, 20) for _ in range(size)]

print("List 1:", list1)
print("List 2:", list2)

combined = list1 + list2
print("Both lists:", combined)

no_duplicates = list(set(list1 + list2))
print("Without duplicates:", no_duplicates)

common = list(set(list1) & set(list2))
print("Common elements:", common)

unique = list(set(list1) ^ set(list2))
print("Unique elements:", unique)

min_max = [min(list1), max(list1), min(list2), max(list2)]
print("Min and max from each list:", min_max)