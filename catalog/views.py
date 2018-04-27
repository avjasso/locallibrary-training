from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre
from django.views import generic

def index(request):
	# View function for home page of site

	# Generate counts of some of the main objects
	num_books = Book.objects.all().count()
	num_instances = BookInstance.objects.all().count()
	# Available books (status = 'a')
	num_instances_available = BookInstance.objects.filter(status__exact='a').count()
	num_authors = Author.objects.count() # The 'all()' is implied by default.
	# Generate counts of existing book genres
	num_genres = Genre.objects.count()
	# Get counts of books with 'the' in the title
	num_books_with_the = Book.objects.filter(title__icontains='the').count()
	# Render the HTML template index.html with the data in the context variable
	return render(
		request,
		'index.html',
		context={'num_books':num_books,'num_instances':num_instances,'num_instances_available':num_instances_available,'num_authors':num_authors, 'num_genres':num_genres, 'num_books_with_the':num_books_with_the},
	)

class BookListView(generic.ListView):
	model = Book

class BookDetailView(generic.DetailView):
	model = Book
