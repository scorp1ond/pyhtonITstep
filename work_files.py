with open("data.txt", "r") as f:
    content = f.read()

with open("backup.txt", "w") as f:
    f.write(content)

with open("data.txt", "r") as f:
    text = f.read()

result = ""

for c in text:
    if "a" <= c <= "z":
        if c == "z":
            result += "a"
        else:
            result += chr(ord(c) + 1)

    elif "A" <= c <= "Z":
        if c == "Z":
            result += "A"
        else:
            result += chr(ord(c) + 1)

    else:
        result += c

with open("encrypted.txt", "w") as f:
    f.write(result)

FILE = "music_collection.txt"

def add_album():
    title = input("Назва: ")
    artist = input("Виконавець: ")
    year = input("Рік: ")

    with open(FILE, "a") as f:
        f.write(title + "|" + artist + "|" + year + "\n")

def show_all():
    try:
        with open(FILE, "r") as f:
            for line in f:
                parts = line.strip().split("|")
                print(parts[0], "-", parts[1], "(", parts[2], ")")
    except FileNotFoundError:
        print("Файл не існує")

def search():
    target = input("Виконавець: ").lower()

    try:
        with open(FILE, "r") as f:
            found = False
            for line in f:
                title, artist, year = line.strip().split("|")
                if artist.lower() == target:
                    print(title, "(", year, ")")
                    found = True
            if not found:
                print("Нічого не знайдено")
    except FileNotFoundError:
        print("Файл не існує")

def delete_album():
    target = input("Назва: ").lower()
    new_lines = []
    deleted = False

    try:
        with open(FILE, "r") as f:
            for line in f:
                title, artist, year = line.strip().split("|")
                if title.lower() != target:
                    new_lines.append(line)
                else:
                    deleted = True

        with open(FILE, "w") as f:
            f.writelines(new_lines)

        if deleted:
            print("Видалено")
        else:
            print("Не знайдено")

    except FileNotFoundError:
        print("Файл не існує")

while True:
    print("\n1 Додати")
    print("2 Показати всі")
    print("3 Пошук")
    print("4 Видалити")
    print("5 Вихід")

    choice = input("Вибір: ")

    if choice == "1":
        add_album()
    elif choice == "2":
        show_all()
    elif choice == "3":
        search()
    elif choice == "4":
        delete_album()
    elif choice == "5":
        break
    else:
        print("Помилка")