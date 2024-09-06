from typing import Self


class Book:
    def __init__(self, isbn: str, title: str, author: str, available=True, checkout_num=0):
        self.__isbn = isbn
        self.__title = title
        self.__author = author
        self.__available = available
        self.__checkout_num = checkout_num

    # Getters
    def get_isbn(self):
        return self.__isbn

    def get_title(self):
        return self.__title

    def get_author(self):
        return self.__author

    def is_available(self):
        return self.__available

    def get_checkout_num(self):
        return self.__checkout_num

    # Setters
    def set_available(self, available: bool) -> None:
        self.__available = available

    def increment_checkout_num(self) -> None:
        self.__checkout_num += 1

    # Utils
    def __str__(self) -> str:
        return f'ISBN: {self.get_isbn()}, Title: {self.get_title()}, Author: {self.get_author()}'

    def __eq__(self, other) -> bool:
        return self.__isbn == other.__isbn
