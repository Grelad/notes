from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('', views.BookListView.as_view(), name='book_list'),
    path('create/', views.CreateBookView.as_view(), name='create_book'),
    path('<pk>/', views.DetailsBookView.as_view(), name='details'),
    path('<pk>/edit', views.EditBookView.as_view(), name='edit_book'),
    path('<pk>/delete', views.DeleteBookView.as_view(), name='delete_book'),
]
