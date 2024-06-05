class Book:
    def __init__(self, title, author) -> None:
        self.book_name = title
        self.author_name = author

    def display_info(self):
        print(f"Book name = {self.book_name} Author = {self.author_name}")