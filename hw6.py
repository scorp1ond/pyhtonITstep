text = input("Enter text: ")
count = 0
for c in text:
    if c in ".!?":
        count += 1
print("Number of sentences:", count)


text = input("\nEnter a string: ")
clean = text.replace(" ", "").lower()

if clean == clean[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")


reserved = ["for", "while", "if", "else", "print"]
text = input("\nEnter text: ")

words = text.split()

for i in range(len(words)):
    if words[i] in reserved:
        words[i] = words[i].upper()

print(" ".join(words))


text = input("\nEnter a string: ")
a = input("First symbol: ")
b = input("Second symbol: ")

i = text.find(a)
j = text.find(b)

if i != -1 and j != -1 and i < j:
    result = text[:i] + text[j+1:]
else:
    result = text

print(result)


text = input("\nEnter text: ")
chars = input("Enter symbols: ")

words = text.split()
result = []

for w in words:
    remove = False
    for c in chars:
        if c in w:
            remove = True
    if not remove:
        result.append(w)

print(" ".join(result))


text = input("\nEnter text: ")

words = text.split()
words.reverse()

print(" ".join(words))