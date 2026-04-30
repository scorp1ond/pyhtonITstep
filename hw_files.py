

f = open("data.txt", "w", encoding="utf-8")
for i in range(3):
    s = input()
    f.write(s + "\n")
f.close()



try:
    f = open("log.txt", "r", encoding="utf-8")
    text = f.read().lower()
    f.close()
except:
    text = ""

words = text.split()

freq = {}

for w in words:
    if w in freq:
        freq[w] += 1
    else:
        freq[w] = 1

top = []

for i in range(10):
    max_word = ""
    max_count = 0

    for w in freq:
        if freq[w] > max_count:
            max_count = freq[w]
            max_word = w

    if max_word == "":
        break

    top.append((max_word, max_count))
    del freq[max_word]

f = open("word_stats.txt", "w", encoding="utf-8")
for word, count in top:
    f.write(word + " " + str(count) + "\n")
f.close()



FILE = "orders.txt"

while True:
    print("1 add")
    print("2 view")
    print("3 find")
    print("4 update")
    print("5 delete")
    print("6 exit")

    c = input()

    match c:
        case "1":
            f = open(FILE, "a", encoding="utf-8")
            num = input()
            name = input()
            qty = input()
            price = input()
            f.write(num + "|" + name + "|" + qty + "|" + price + "\n")
            f.close()

        case "2":
            try:
                f = open(FILE, "r", encoding="utf-8")
                for line in f:
                    print(line.strip())
                f.close()
            except:
                pass

        case "3":
            num = input()
            try:
                f = open(FILE, "r", encoding="utf-8")
                for line in f:
                    if line.split("|")[0] == num:
                        print(line.strip())
                f.close()
            except:
                pass

        case "4":
            num = input()
            lines = []

            try:
                f = open(FILE, "r", encoding="utf-8")
                lines = f.readlines()
                f.close()
            except:
                pass

            f = open(FILE, "w", encoding="utf-8")

            for line in lines:
                p = line.strip().split("|")
                if p[0] == num:
                    p[2] = input()
                    p[3] = input()
                    f.write("|".join(p) + "\n")
                else:
                    f.write(line)

            f.close()

        case "5":
            num = input()
            lines = []

            try:
                f = open(FILE, "r", encoding="utf-8")
                lines = f.readlines()
                f.close()
            except:
                pass

            f = open(FILE, "w", encoding="utf-8")

            for line in lines:
                if line.split("|")[0] != num:
                    f.write(line)

            f.close()

        case "6":
            break

        case _:
            print("error")