from django.test import TestCase
from utils.providers.goodreads.client import (
    Client as GrClient
)
class ProviderGoodreadsTests(TestCase):

    # def setUp(self):

    def test_books_on_shelf_count(self):
        books_read = GrClient().books_on_shelf_count('read-2019')
        self.assertTrue(
            isinstance(books_read, int)
        )
    def test_for_no_shelf(self):
        books_read = GrClient().books_on_shelf_count('read-1981')
        self.assertTrue(
            books_read == GrClient().no_shelf_code
        )