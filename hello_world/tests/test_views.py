from django.test import TestCase
from django.urls import reverse, reverse_lazy

from hello_world.models import Book, Author


class TestBookView(TestCase):
    def setUp(self) -> None:
        self.book = Book.objects.create(
            **{'name': 'TestBook', 'year': 1806}
        )
        self.author = Author.objects.create(**{'name': 'TestAuthor'})
        self.author.books.add(self.book)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/books/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_accessible_by_name(self):
        resp = self.client.get(reverse('book_list'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('book_list'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'book_list.html')

    def test_get_book_details(self):
        url = reverse('details', args=(self.book.id,))
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)

    def test_get_non_exist_book_details(self):
        url = reverse('details', args=(2,))
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 404)
