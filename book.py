#!/usr/bin/env python3


class Book:
    """A book in the bookstore that can be read online."""

    def __init__(self, title, page_count):
        self.title = title
        self.page_count = page_count  # goes through the setter below

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        # Only accept whole numbers for the page count
        if isinstance(value, int):
            self._page_count = value
        else:
            print("page_count must be an integer")

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")