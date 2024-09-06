from typing_extensions import Self


class Book:
    def __init__(self, isbn: str, title: str, author: str, available: bool = True, checkout_num: int = 0) -> None:
        self.__isbn = isbn
        self.__title = title
        self.__author = author
        self.__available = available
        self.__checkout_num = checkout_num

    # Getters
    def get_isbn(self) -> str:
        return self.__isbn

    def get_title(self) -> str:
        return self.__title

    def get_author(self) -> str:
        return self.__author

    def is_available(self) -> bool:
        return self.__available

    def get_checkout_num(self) -> int:
        return self.__checkout_num

    # Setters
    def set_available(self, available: bool) -> None:
        self.__available = available

    def increment_checkout_num(self) -> None:
        self.__checkout_num += 1

    # Utils
    def __str__(self) -> str:
        return f'ISBN: {self.get_isbn()}, Title: {self.get_title()}, Author: {self.get_author()}'

    def __eq__(self: Self, other: object) -> bool:
        if not isinstance(other, Book):
            return False
        return other.get_isbn() == self.get_isbn()
