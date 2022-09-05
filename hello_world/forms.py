from django import forms
from .models import Book
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class BookForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'id-editBook'
        self.helper.form_class = 'form-inline'
        self.helper.form_method = 'post'
        self.helper.form_tag = False
        self.helper.add_input(Submit('submit', 'Save'))
        self.helper.use_custom_control = False

    class Meta:
        model = Book
        fields = '__all__'


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
