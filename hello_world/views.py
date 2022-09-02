from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views import View
from .forms import BookForm
from .models import Book
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView


class BookListView(View):

    def get(self, request):
        self.context = {'books': Book.objects.all()}
        return render(request, 'book_list.html', self.context)


class CreateBookView(CreateView):
    model = Book
    fields = '__all__'
    template_name = 'book_form.html'
    success_url = reverse_lazy('book_list')


class DetailsBookView(DetailView):
    model = Book
    template_name = 'details_book.html'


class EditBookView(UpdateView):
    model = Book
    fields = '__all__'
    template_name = 'edit_book.html'

    def get_success_url(self):
        return reverse_lazy('edit_book', kwargs={'pk': self.object.pk})


class DeleteBookView(DeleteView):
    model = Book
    template_name = 'book_confirm_delete.html'
    success_url = reverse_lazy('book_list')
