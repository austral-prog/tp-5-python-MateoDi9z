from typing import List
from typing_extensions import Self

from src.Book import Book
from src.User import User


class Library:
    __books: List[Book]

    def __init__(self) -> None:
        self.__books = []
        self.__users = []
        self.__checked_out_books = []
        self.__checked_in_books = []

    # Getters
    def get_books(self) -> List[Book]:
        return self.__books

    def get_users(self) -> List[User]:
        return self.__users

    def get_checked_out_books(self) -> list:
        return self.__checked_out_books

    def get_checked_in_books(self) -> list:
        return self.__checked_in_books

    # 1.1 Add Book
    def add_book(self, isbn: str, title: str, author: str) -> None:
        book = Book(isbn, title, author)
        books = self.get_books()

        if len(books) > 0:
            for old_book in books:
                if old_book.get_isbn() == isbn:
                    return

        self.__books.append(book)

    # 1.2 List All Books
    def list_all_books(self) -> None:
        for book in self.__books:
            print(f"ISBN: {book.get_isbn()}, Title: {book.get_title()}, Author: {book.get_author()}")

    # 2.1 Check out book
    def check_out_book(self, isbn: str, dni: int, due_date: str) -> str:
        book = self.find_book(isbn)
        user = self.find_user(dni)

        if (not isinstance(book, Book)) or (not isinstance(user, User)):
            return f"Unable to find the data for the values: ISBN {isbn} and DNI: {dni}"

        if not book.is_available():
            return f"Book {isbn} is not available"

        self.__checked_out_books.append([isbn, dni, due_date])
        book.set_available(False)
        return f"User {dni} checked out book {isbn}"

    # 2.2 Check in book
    def check_in_book(self, isbn: str, dni: int, returned_date: str) -> str:
        book = self.find_book(isbn)

        if book.is_available():
            return f"Book {isbn} is not available"

        new_books: list = []
        for old_book in self.get_checked_out_books():
            if old_book[0] == isbn:
                continue
            new_books.append(old_book)

        self.__checked_out_books = new_books
        self.__checked_in_books.append([isbn, dni, returned_date])
        book.set_available(True)
        return f"Book {isbn} checked in by user {dni}"

    # Utils
    def add_user(self, dni: int, name: str) -> None:
        user = User(dni, name)
        users = self.get_users()

        if len(users) > 0:
            for old_users in users:
                if old_users.get_dni() == dni:
                    return

        self.__users.append(user)

    def find_user(self, dni: int) -> bool | User:
        if not len(self.get_users()):
            return False
        for user in self.get_users():
            if user.get_dni() == dni:
                return user
        return False

    def find_book(self, isbn: str) -> bool | Book:
        if not len(self.get_books()):
            return False
        for book in self.get_books():
            if book.get_isbn() == isbn:
                return book
        return False
