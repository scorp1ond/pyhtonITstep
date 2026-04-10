class book:
    def __init__(self, title, authors, year):
        self.title = title
        self.authors = authors
        self.year = year

    def __str__(self):
        return f"title: {self.title}, authors: {', '.join(self.authors)}, year: {self.year}"

class library:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.books = []

    def __str__(self):
        return f"library: {self.name}, address: {self.address}"

    def show_books(self):
        if count(self.books) ==0:
            print("no books available")
        else:
            for b in self.books:
                print(b)

    def add_book(self, book):
        self.books.append(book)
        print("book added")

    def remove_book(self, title):
        for b in self.books:
            if b.title.lower() ==title.lower():
                self.books.remove(b)
                print("book removed")
                return
        print("book not found")

    def find_by_title(self, title):
        for b in self.books:
            if b.title.lower() ==title.lower():
                print(b)
                return
        print("book not found")

    def find_by_author(self, author):
        found = False
        for b in self.books:
            for a in b.authors:
                if a.lower() ==author.lower():
                    print(b)
                    found = true
        if not found:
            print("no books found")

lib = library("central library", "main street 1")

while True:
    print("\nmenu:")

    print("1 add book")
    print("2remove book")
    print("3 show all books")
    print("4 find book by title")
    print("5 find books by author")
    print("0 exit")

    choice = input("choose option: ")
    match choice:
        case "1":
            title = input("enter title: ")
            authors = input("enter authors: ").split(",")
            authors = [a.strip() for a in authors]
            year = input("enter year: ")
            new_book = book(title, authors, year)
            lib.add_book(new_book)
        case "2":
            title = input("enter title to remove: ")
            lib.remove_book(title)
        case "3":
            lib.show_books()
        case "4":
            title = input("enter title:")
            lib.find_by_title(title)
        case "5":
            author = input("enter author: ")
            lib.find_by_author(author)
        case "0":
            print("exit")
            break
        case _:
            print("wrong option")