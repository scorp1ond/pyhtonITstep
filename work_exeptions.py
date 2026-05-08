# Task 1 — discount price

try:
    price = float(input("Price: "))
    discount = float(input("Discount %: "))

    final_price = price - price * discount / 100
    print(final_price)

except ValueError:
    print("Invalid input")


# Task 2 — currency conversion

try:
    usd = float(input("USD: "))
    rate = float(input("EUR rate: "))

    if rate == 0:
        raise Exception("Rate cannot be zero")

    eur = usd * rate
    print(eur)

except ValueError:
    print("Invalid input")

except Exception as e:
    print(e)

finally:
    print("Done")


# Task 3 — grades average

try:
    grades = input("Grades: ").split()
    nums = [int(x) for x in grades]

    avg = sum(nums) / len(nums)
    print(avg)

except ValueError:
    print("Invalid number")

except ZeroDivisionError:
    print("Empty list")

finally:
    print("Done")


# Task 4 — ATM

balance = 1000

try:
    amount = int(input("Withdraw: "))

    if amount % 10 != 0 or amount > balance:
        raise Exception("Invalid amount")

    balance -= amount
    print(balance)

except ValueError:
    print("Invalid input")

except Exception as e:
    print(e)

finally:
    print("Transaction ended")


# Task 5 — order number

try:
    order = input("Order: ")

    if not order.startswith("ORD") or not order[3:].isdigit():
        raise Exception("Wrong format")

    print("OK")

except Exception as e:
    print(e)

finally:
    print("Check finished")


# Task 6 — numbers processing

try:
    data = input("Numbers: ").split()
    nums = []

    for x in data:
        try:
            nums.append(int(x))
        except ValueError:
            print("Skip:", x)

    total = sum(nums)
    avg = total / len(nums)

    print(total, avg)

except ZeroDivisionError:
    print("No valid numbers")

finally:
    print("Done")