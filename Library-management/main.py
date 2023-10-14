from library import Library

def main():
    my_library = Library()
    my_library.load_from_file()

    # Your code to interact with the library
    # For example, adding books, removing books, etc.

    my_library.save_to_file()

if __name__ == "__main__":
    main()
