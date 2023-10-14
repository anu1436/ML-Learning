import json

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, category):
        book = {'title': title, 'author': author, 'category': category}
        self.books.append(book)

    def remove_book(self, title):
        for book in self.books:
            if book['title'] == title:
                self.books.remove(book)
                return f"Removed {title} from the library."
        return "Book not found."

    def list_books(self, category=None):
        if category:
            return [book for book in self.books if book['category'] == category]
        return self.books

    def search_book(self, query):
        return [book for book in self.books if query.lower() in book['title'].lower() or query.lower() in book['author'].lower()]

    def save_to_file(self):
        with open('library.json', 'w') as f:
            json.dump(self.books, f)

    def load_from_file(self):
        try:
            with open('library.json', 'r') as f:
                self.books = json.load(f)
        except FileNotFoundError:
            self.books = []

    def export_physics_books_to_txt(self):
        with open('physics_books.txt', 'w') as f:
            for book in self.list_books("Physics"):
                f.write(f"{book['title']} by {book['author']}\n")

# Initialize library and load data from file
my_library = Library()
my_library.load_from_file()

# Add some physics books
my_library.add_book("A Brief History of Time", "Stephen Hawking", "Physics")
my_library.add_book("The Elegant Universe", "Brian Greene", "Physics")

# Export physics books to a text file
my_library.export_physics_books_to_txt()

# Save to file
my_library.save_to_file()
