from django.contrib import admin

# Register your models here.
from .models import Author, Genre, Book, BookInstance,Language

#admin.site.register(Book)


class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
    extra=0

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
   list_display= ('title','author','display_genre')
   inlines = [BooksInstanceInline]
  

# admin.site.register(Author)
class BooksInline(admin.TabularInline):
    model = Book
    extra=0
    

# Define the admin class
class AuthorAdmin(admin.ModelAdmin):
   list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
   fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
   inlines= [BooksInline]

# Register the admin class with the associated model
admin.site.register(Author, AuthorAdmin)

#admin.site.register(BookInstance)
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('id','book','status','borrower','due_back')
    list_filter = ('status', 'due_back')
    fieldsets = (
        ('Datos del libro', {
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', {
            'fields': ('status', 'due_back','borrower')
        }),
    )



admin.site.register(Language)
admin.site.register(Genre)
