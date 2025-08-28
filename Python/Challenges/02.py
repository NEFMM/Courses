# Develop a program that creates a book with the attributes such as title, author and year of publication. 
# Then write a program create an array of books, fill it with some books and then print the title of the oldest book.

class book:
    def __init__(self, title, author, year):
          self.title = title
          self.author = author
          self.year = year

def find_oldest_book(books_list):
    oldest_book = books_list[0]
    for book in books_list[1:]:
        if book.year < oldest_book.year:
            oldest_book = book
    return oldest_book

books = [
    book("To Kill a Mockingbird", "Harper Lee", 1960),
    book("1984", "George Orwell", 1949),
    book("Pride and Prejudice", "Jane Austen", 1813),
    book("The Hobbit", "J.R.R. Tolkien", 1937),
    book("Dune", "Frank Herbert", 1965),
]

oldest_book_found = find_oldest_book(books)

if oldest_book_found:
    print(f"The oldest book is: {oldest_book_found.title}")
else:
    print(f"The list is empty")