import asyncio

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from .forms import BookForm, RegisterForm
from .models import Book
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from tg_api.bot import handler
from asgiref.sync import sync_to_async, async_to_sync
from django.utils.decorators import classonlymethod


class BookListView(View):

    def get(self, request):
        self.context = {'books': Book.objects.all()}
        return render(request, 'book_list.html', self.context)


class CreateBookView(View):
    model = Book
    form_class = BookForm
    template_name = 'book_form.html'
    success_url = reverse_lazy('book_list')
    # login_url = '/login/'
    # redirect_field_name = 'redirect_to'

    @classonlymethod
    def as_view(cls, **initkwargs):
        view = super().as_view(**initkwargs)
        view._is_coroutine = asyncio.coroutines._is_coroutine
        return view

    async def get(self, request,  *args, **kwargs):
        form = BookForm()
        return render(
            request,
            self.template_name,
            {
              'form': form,
              "is_authenticated": await sync_to_async(lambda: request.user.is_authenticated)()
            }
        )

    async def post(self, request, *args, **kwargs):
        form = BookForm(request.POST)
        if form.is_valid():
            await sync_to_async(form.save)()
            await handler(form.cleaned_data)
            return redirect(self.success_url)
        return render(request, self.template_name, {'form': form})


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
