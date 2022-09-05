from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from .forms import BookForm, RegisterForm
from .models import Book
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


class BookListView(View):

    def get(self, request):
        self.context = {'books': Book.objects.all()}
        return render(request, 'book_list.html', self.context)


class CreateBookView(LoginRequiredMixin, CreateView):
    model = Book
    form_class = BookForm
    template_name = 'book_form.html'
    success_url = reverse_lazy('book_list')
    login_url = '/login/'
    redirect_field_name = 'redirect_to'


class DetailsBookView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Book
    template_name = 'details_book.html'
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    permission_required = ('hello_world.view_book', )
    permission_denied_message = 'You shell not pass!'


class EditBookView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'edit_book.html'
    login_url = '/login/'
    redirect_field_name = 'redirect_to'
    permission_required = ('hello_world.view_book', 'hello_world.change_book')


    def get_success_url(self):
        return reverse_lazy('edit_book', kwargs={'pk': self.object.pk})


class DeleteBookView(LoginRequiredMixin, DeleteView):
    model = Book
    template_name = 'book_confirm_delete.html'
    success_url = reverse_lazy('book_list')
    login_url = '/login/'
    redirect_field_name = 'redirect_to'


def sign_up(request):
    if request.POST:
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('book_list')
    else:
        form = RegisterForm()
    return render(request, 'registration/sign_up.html', {'form': form})
