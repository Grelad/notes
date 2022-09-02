from django.test import TestCase

from hello_world.models import Book, Author


class TestBookModel(TestCase):

    def setUp(self) -> None:
        self.book = Book.objects.create(
            **{'name': 'TestBook', 'year': 1806}
        )
        self.author = Author.objects.create(**{'name': 'TestAuthor'})
        self.author.books.add(self.book)

    def test_get_book(self):
        import pdb
        pdb.set_trace()
        book = Book.objects.get(id=self.book.id)
        self.assertEqual(book.name, 'TestBook')
        self.assertTrue(book.author_set.all(), self.author)
