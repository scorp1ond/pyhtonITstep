
contacts = {}

while True:
    print("\n1 Add contact")
    print("2 Delete contact")
    print("3 Edit contact")
    print("4 Show all contacts")
    print("0 Exit")

    choice = input("Choose: ")

    if choice == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        contacts[name] = phone

    elif choice == "2":
        name = input("Name: ")
        if name in contacts:
            del contacts[name]

    elif choice == "3":
        name = input("Name: ")
        if name in contacts:
            phone = input("New phone: ")
            contacts[name] = phone

    elif choice == "4":
        print(contacts)

    elif choice == "0":
        break



text = input("Enter text: ").lower().split()

count = {}

for word in text:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1

print(count)


# Task 3 — currency converter

rates = {"USD": 40.2, "EUR": 42.5, "PLN": 9.6}

currency = input("Currency: ")
amount = float(input("Amount in UAH: "))

if currency in rates:
    print(amount / rates[currency])


dict_eng = {
    "hello": "привіт",
    "cat": "кіт",
    "dog": "собака"
}

word = input("Word: ").lower()

if word in dict_eng:
    print(dict_eng[word])
else:
    print("Not found")