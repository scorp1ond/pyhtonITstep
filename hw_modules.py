import random
import string

name = input("Base name: ")

nick1 = name + str(random.randint(100, 9999))

sep = random.choice(["_", ".", "-"])
letters = "".join(random.choices(string.ascii_lowercase, k=3))
nick2 = name + sep + letters

prefixes = ["Pro", "Super", "Ultra"]
prefix = random.choice(prefixes)
digits = str(random.randint(10, 99))
nick3 = prefix + name.capitalize() + digits


print("\nNICKNAME OPTIONS")
print(nick1)
print(nick2)
print(nick3)


def draw_header(title):
    width = 40
    print("=" * width)
    print(title.center(width))
    print("=" * width)


def draw_menu(options):
    for i in range(len(options)):
        print(f"[ {i+1} ] {options[i]}")

def draw_warning(message):
    print("!!! " + message + " !!!")

print("\n")

draw_header("MY GAME")

menu = ["Start game", "Settings", "Exit"]
draw_menu(menu)

choice = input("Choose option: ")

if choice not in ["1", "2", "3"]:
    draw_warning("Wrong option selected")
else:
    print("Selected:", menu[int(choice) - 1])