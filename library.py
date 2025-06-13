
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True


    def __str__(self):
        if self.available:
            status = "доступна"
        else:
            status = "выдана"
        return  f'"{self.title}" - {self.author} : {status}'


    def borrow(self):
        if self.available:
            self.available = False
            return f'Книга "{self.title}" выдана'
        return f'Книга "{self.title}" выдана, взять нельзя'


    def return_book(self):
        if not self.available:
            self.available = True
            return f'Книга "{self.title}" возвращена'
        return f'Книга "{self.title}" еще не выдана'


class Library:
    def __init__(self):
        self.books = {}


    def add_book(self, book):
        self.books[book.title] = book


    def show_books(self):
        if self.books:
            print(f'Список книг:')
            for book in self.books.values():
                print(f' {book}')
        else:
            print(f'Книг нет')


    def borrow_book(self, title):
        book = self.books.get(title)
        if book:
            print(book.borrow())
        else:
            print(f'Такой книги "{title}" нет в библиотеке')


    def return_book(self, title):
        book = self.books.get(title)
        if book:
            print(book.return_book())
        else:
            print(f'Такой книги "{title}" нет в библиотеке')


if __name__ == "__main__":

    book1 = Book("1", "Толстой")
    book2 = Book("2", "Маяковский")
    book3 = Book("3", "Пушкин")
    book4 = Book("4", "Лесков")



    library = Library()
    library.add_book(book1)
    library.add_book(book2)
    library.add_book(book3)
    library.add_book(book4)

    library.show_books()

    library.borrow_book("1")
    library.borrow_book("3")

    library.return_book("1")

    library.borrow_book("5")

    library.borrow_book("3")

    library.show_books()