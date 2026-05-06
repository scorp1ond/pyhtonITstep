
contacts = {}

while True:
    print("\n1 add")
    print("2 delete")
    print("3 edit")
    print("4 show")
    print("5 exit")

    choice = input("choose: ")

    if choice == "1":
        name = input("name: ")
        phone = input("phone: ")
        contacts[name] = phone

    elif choice == "2":
        name = input("name: ")
        if name in contacts:
            del contacts[name]

    elif choice == "3":
        name = input("name: ")
        if name in contacts:
            phone = input("new phone: ")
            contacts[name] = phone

    elif choice == "4":
        print(contacts)

    elif choice == "5":
        break


text = input("\ntext: ").lower().split()

words = {}

for w in text:
    if w in words:
        words[w] += 1
    else:
        words[w] = 1

print(words)



rates = {"USD": 40.2, "EUR": 42.5, "PLN": 9.6}

currency = input("\ncurrency: ")
amount = float(input("uah: "))

if currency in rates:
    print(amount / rates[currency])
else:
    print("no currency")



dict_words = {
    "hello": "привіт",
    "world": "світ",
    "book": "книга",
    "cat": "кіт"
}

word = input("\nword: ").lower()

if word in dict_words:
    print(dict_words[word])
else:
    print("not found")
