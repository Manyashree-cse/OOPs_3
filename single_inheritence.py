class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def display_book_details(self):
        return f"'{self.title}' by {self.author}"
    
class Issuebook(Book):
    def __init__(self,tite, author, issued_to,issued_date):
        super().__init__(tite, author)
        self.issued_to = issued_to
        self.issued_date = issued_date

    def display_book_details(self):
        book_details = super().display_book_details()
        return f"{book_details}"
    
    def  display_issued_book_details(self):
        return f"'{self.title}' by {self.author}, issued to {self.issued_to} on {self.issued_date}"
    
# Example usage:
book1 = Book("1984", "George Orwell")
print(book1.display_book_details())
issued_book1 = Issuebook("To Kill a Mockingbird", "Harper Lee", "Alice", "2024-06-15")
print(issued_book1.display_issued_book_details())