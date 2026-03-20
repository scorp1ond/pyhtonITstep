dictionary = {
    "cat": "кіт",
    "dog": "собака",
    "house": "будинок",
    "car": "автомобіль",
    "apple": "яблуко"
}

word = input().lower()

if word in dictionary:
    print(dictionary[word])
else:
    print("Слово не знайдено")

n = int(input())

my_games = set(input().lower().split(", "))

common_games = my_games.copy()

for i in range(n):
    games = set(input().lower().split(", "))
    common_games = common_games.intersection(games)

if common_games:
    print(", ".join(common_games))
else:
    print("Немає спільних ігор")