class Book:
    # Class variable to keep track of all book instances
    all_books = []

    def __init__(self, title):
        self.title = title
        # Add the current book instance to the class variable
        self.__class__.all_books.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise Exception("Title must be a string")
        self._title = value


class Author:
    # Class variable to keep track of all author instances
    all_authors = []

    def __init__(self, name):
        self.name = name
        # Add the current author instance to the class variable
        self.__class__.all_authors.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception("Author's name must be a string")
        self._name = value


class Contract:
    # Class variable to keep track of all contract instances
    all_contracts = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        # Add the current contract instance to the class variable
        self.__class__.all_contracts.append(self)

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception("Author must be an instance of Author class")
        self._author = value

    @property
    def book(self):
        return self._book

    @book.setter
    def book(self, value):
        if not isinstance(value, Book):
            raise Exception("Book must be an instance of Book class")
        self._book = value

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if not isinstance(value, str):
            raise Exception("Date must be a string")
        self._date = value

    @property
    def royalties(self):
        return self._royalties

    @royalties.setter
    def royalties(self, value):
        if not isinstance(value, int):
            raise Exception("Royalties must be an integer")
        self._royalties = value


# Example usage:
if __name__ == "__main__":
    author1 = Author("John Doe")
    book1 = Book("Python Programming")
    contract1 = Contract(author1, book1, "2024-03-13", 10)

    print("Book:", contract1.book.title)
    print("Author:", contract1.author.name)
    print("Date:", contract1.date)
    print("Royalties:", contract1.royalties)
