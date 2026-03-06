def fig_a(n):
    for i in range(n):
        for j in range(n):
            if j >= i:
                print("*", end="")
            else:
                print(" ", end="")
        print()

def fig_b(n):
    for i in range(n):
        for j in range(n):
            if j <= i:
                print("*", end="")
            else:
                print(" ", end="")
        print()

def fig_c(n):
    for i in range(n):
        for j in range(n):
            if i + j <= n - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()

def fig_d(n):
    for i in range(n):
        for j in range(n):
            if i + j >= n - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()

def fig_x(n):
    for i in range(n):
        for j in range(n):
            if j == i or j == n - i - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()


n = int(input("Enter size: "))

print("Menu:")
print("1 - A")
print("2 - B")
print("3 - C")
print("4 - D")
print("5 - X")

choice = int(input("Choose figure: "))

if choice == 1:
    fig_a(n)
elif choice == 2:
    fig_b(n)
elif choice == 3:
    fig_c(n)
elif choice == 4:
    fig_d(n)
elif choice == 5:
    fig_x(n)
else:
    print("Wrong choice")