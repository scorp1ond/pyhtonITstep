dictionary = {
    "apple": "яблуко",
    "book": "книга",
    "car": "автомобіль",
    "house": "будинок",
    "dog": "собака"
}

word = input().lower()

if word in dictionary:
    print(dictionary[word])
else:
    print("not found")

n = int(input())

common = input().lower().split()

for i in range(n):
    games = input().lower().split()
    new_common = []

    for g in common:
        if g in games:
            new_common.append(g)

    common = new_common

if len(common) > 0:
    for g in common:
        print(g)
else:
    print("no common games")