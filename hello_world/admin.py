from django.contrib import admin

# Register your models here.
from .models import Book, Author
from django.utils.html import format_html


class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'year', 'show_year_bigger_than_1900')
    list_filter = ('year', )
    search_fields = ('name__startswith', )
    fields = ('name',)

    class Meta:
        ordering = ('year', )

    def show_year_bigger_than_1900(self, obj):
        books = Book.objects.filter(year__gt=1900)
        return format_html('<strong><i>{}</i></strong>', books)

    show_year_bigger_than_1900.short_description = 'List of books'


admin.site.register(Book, BookAdmin)
admin.site.register(Author)
