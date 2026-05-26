class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True


class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title, author)
        self.file_size = file_size


class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, title):
        self.books = [book for book in self.books if book.title != title]

    def issue_book(self, title, member):
        for book in self.books:
            if book.title == title and book.available:
                book.available = False
                member.borrowed_books.append(book.title)
                print(f"{title} issued to {member.name}")
                return

        print("Book not available")

    def return_book(self, title, member):
        for book in self.books:
            if book.title == title:
                book.available = True
                member.borrowed_books.remove(title)
                print(f"{title} returned")

    def list_available_books(self):
        for book in self.books:
            if book.available:
                print(book.title)


library = Library()

book1 = Book("Python Basics", "John Doe")
ebook1 = EBook("AI Guide", "Jane Smith", "5MB")
member1 = Member("Alice")

library.add_book(book1)
library.add_book(ebook1)

library.issue_book("Python Basics", member1)
library.list_available_books()