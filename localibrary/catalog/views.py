from django.shortcuts import render
from .models import Author, Book, BookInstance, Genre
from django.views import generic


# Create your views here.
def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'A')
    num_instances_available = BookInstance.objects.filter(status__exact='A').count()

    # Available books (contains a word)
    num_programming_books = Book.objects.filter(title__contains='Program').count()

    # Number of available genres
    num_genres = Genre.objects.count()

    # The 'all()' is implied by default
    num_authors = Author.objects.count()

    # Number of visits to this view, as counted in the session variable.
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_programming_books': num_programming_books,
        'num_genres': num_genres,
        'num_visits': num_visits,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


class BookListView(generic.ListView):
    """ A class that inherits the generic ListView.
    The generic view will query the database to get all records for the specified model (Book)
    then render a template located at localibrary/catalog/templates/catalog/book_list.html
    """
    model = Book
    paginate_by = 10


class BookDetailView(generic.DetailView):
    model = Book


class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 10


class AuthorDetailView(generic.DetailView):
    model = Author
