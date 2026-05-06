import random
import math

try:
    a = float(input("A: "))
    b = float(input("B: "))
    print("Result:", a / b)

except ValueError:
    print("Not a number")

except ZeroDivisionError:
    print("Cannot divide by 0")

finally:
    print("Done task 1")


lst = [10, 20, 30, 40, 50]

try:
    i = int(input("Index: "))
    print(lst[i])

except ValueError:
    print("Not a number")

except IndexError:
    print("Wrong index")

finally:
    print("Done task 2")

try:
    data = input("Sales: ")
    nums = data.split()

    total = 0
    for x in nums:
        total += int(x)

    print("Sum:", total)

except ValueError:
    print("Wrong input")

finally:
    print("Done task 3")

try:
    n = float(input("Number: "))

    if n < 0:
        raise Exception("No sqrt for negative")

    print("Result:", math.sqrt(n))

except ValueError:
    print("Not a number")

except Exception as e:
    print(e)

finally:
    print("Done task 4")


try:
    data = input("Product (name, price, count): ")
    parts = data.split(",")

    name = parts[0].strip()
    price = float(parts[1].strip())
    count = int(parts[2].strip())

    print("OK:", name, price * count)

except ValueError:
    print("Wrong data")

finally:
    print("Done task 5")


def connect_to_server():
    if random.randint(0, 1) == 0:
        return "Connected"
    else:
        raise ConnectionError("Fail")

try:
    print(connect_to_server())

except ConnectionError:
    print("Failed to connect")

finally:
    print("Done task 6")
