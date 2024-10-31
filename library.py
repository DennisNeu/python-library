from book import Book

class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self, title, author):
        self.books.append(Book(title, author))

    def return_book(self):
        pass

    def borrow_book(self):
        pass

    def view_books(self):
        for index, book in enumerate(self.books):
            print(f"{index + 1}: {book}")