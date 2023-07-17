import json
from pprint import pprint

from demoqa_collection.book_store_application.pages.page_book_store_api import PageBookStore


class TestGetBooks:

    def test_get_book(self):
        page = PageBookStore()
        status = page.get_books().status_code
        authors = None
        if status == 200:
            content = json.loads(page.get_books().content)
            authors = set([book.get('author') for book in content.get('books')])
            for author in authors:
                print(author)
        assert len(authors) == 8


    def test_(self):
        page = PageBookStore()
        pass
