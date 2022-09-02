from django.test import TestCase

from hello_world.forms import BookForm


class TestBookForm(TestCase):

    # def setUp(self) -> None:
    #     self.form = BookForm()

    def test_name_validation(self):
        form = BookForm(
            {
                'name': '12345678901234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901',
                'year': -1500
            }
        )
        self.assertTrue(form.errors)
