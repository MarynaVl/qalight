import requests


class PageBookStore:
    url = 'https://demoqa.com'

    def __init__(self):
        self.books = requests.get(self.url + '/BookStore/v1/Books')

    def get_books(self):
        return self.books

