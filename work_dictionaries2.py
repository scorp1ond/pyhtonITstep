import random


nums = list(map(int, input("Enter numbers: ").split()))
print(set(nums))




a = set()
b = set()

for _ in range(10):
    a.add(random.randint(1, 20))
    b.add(random.randint(1, 20))

print("Set A:", a)
print("Set B:", b)

print("Common:", a & b)
print("Difference A-B:", a - b)
print("Union:", a | b)



w1 = input("Word 1: ").lower()
w2 = input("Word 2: ").lower()

print(sorted(w1) == sorted(w2))