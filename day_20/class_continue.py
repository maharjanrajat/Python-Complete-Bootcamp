# Create a class called Book that has book_name and author_name as property. Also create class called Library that has property called books that consist of list of books and create a method name add_book that adds book to the library. Instantiate the Library class and add book. 

# import book
from book import Book
from library import Library

book_title = input("Enter book name:")
book_author = input('Enter book author:')

b1 = Book(book_title, book_author)

library = Library()
library.add_book(b1)

print("Total books in the library is ", library.book_count())

library.display_books()


while True:
    print("Choose an option")
        