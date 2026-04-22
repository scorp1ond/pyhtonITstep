def print_quote():
    print('"Don\'t compare yourself with anyone in this world.')
    print('If you do so, you are insulting yourself."')
    print('Bill Gates')


def print_even(a, b):
    start = min(a, b)
    end = max(a, b)
    
    for i in range(start, end + 1):
        if i % 2 == 0:
            print(i, end=' ')
    print()


def draw_square(size, symbol, filled):
    for i in range(size):
        for j in range(size):
            if filled or i == 0 or i == size - 1 or j == 0 or j == size - 1:
                print(symbol, end=' ')
            else:
                print(' ', end=' ')
        print()


def count_digits(n):
    return len(str(n).replace('-', ''))



def is_palindrome(n):
    s = str(n)
    return s == s[::-1]


print_quote()

print_even(2, 10)

draw_square(5, '*', True)
print()
draw_square(5, '*', False)

print(count_digits(3456))      # 4
print(count_digits(-12345))    # 5

print(is_palindrome(123321))   # True
print(is_palindrome(12321))    # True
print(is_palindrome(421987))   # False