
def show_text():
    print('"Don’t let the noise of others’ opinions drown out your own inner voice."')
    print("Steve Jobs")


show_text()


def odd_numbers(a, b):
    for i in range(a, b + 1):
        if i % 2 != 0:
            print(i, end=" ")


odd_numbers(1, 10)


def draw_line(length, direction, symbol):
    if direction == "h":
        print(symbol * length)
    elif direction == "v":
        for i in range(length):
            print(symbol)


draw_line(10, "h", "*")
draw_line(5, "v", "#")


def max_of_four(a, b, c, d):
    return max(a, b, c, d)


print(max_of_four(5, 9, 2, 7))


def is_prime(num):
    if num < 2:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


print(is_prime(7))
print(is_prime(10))


def is_lucky(num):
    num = str(num)

    first = int(num[0]) + int(num[1]) + int(num[2])
    second = int(num[3]) + int(num[4]) + int(num[5])

    return first == second


print(is_lucky(123420))
print(is_lucky(723422))