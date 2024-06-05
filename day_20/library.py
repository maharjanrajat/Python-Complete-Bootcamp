
class Library:
    def __init__(self) -> None:
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def book_count(self):
        return len(self.books)
    
    def display_books(self):
        for book in self.books:
            book.display_info()

