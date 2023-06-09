from django.http import HttpResponseRedirect
from django.shortcuts import render
from BooksApp.queries import Queries

repo_name = 'books'
port = 7200
endpoint = f'http://localhost:{port}'


def index(request):
    return render(request, 'base.html')


def books(request):
    q = Queries(endpoint, repo_name)
    books = q.get_all_books()
    return render(request, 'books.html', {'books': books})


def home(request):
    q = Queries(endpoint, repo_name)
    nBad = q.get_number_bad_books()
    nGood = q.get_number_good_books()
    nBooks = q.get_number_books()
    nShort = q.get_number_short_books()
    nLong = q.get_number_long_books()
    nPopular = q.get_number_popular_books()
    nSeen = q.get_number_seen_books()

    return render(request, 'index.html',
                  {'nBad': nBad, 'nGood': nGood, 'nBooks': nBooks, 'nShort': nShort, 'nLong': nLong,
                   'nPopular': nPopular, 'nSeen': nSeen})


def book(request, book_isbn):
    q = Queries(endpoint, repo_name)
    book = q.get_book_by_isbn(book_isbn)

    return render(request, 'book.html', {'book': book})


def update(request, book_isbn):
    q = Queries(endpoint, repo_name)
    q.update_seen(book_isbn)
    # send back to the book page
    url = '/books/' + str(book_isbn) + '/'
    return HttpResponseRedirect(url)


def author(request, author_name):
    q = Queries(endpoint, repo_name)
    author = q.get_books_by_author(author_name)
    return render(request, 'author.html', {'author': author, 'author_name': author_name})


def search_books(request):
    q = Queries(endpoint, repo_name)
    keyword = request.GET.get('searchForm')
    print(f"key: {keyword}")
    title = f"Results for key: {keyword}"
    books = q.search_book(keyword)
    return render(request, 'search.html', {'title': title, "books": books})


def search_books_by_years(request):
    q = Queries(endpoint, repo_name)
    year1 = request.GET.get('year1')
    year2 = request.GET.get('year2')
    print(f"key: {year1} {year2}")
    title = f"Results for years: {year1} to {year2}"
    books = q.search_year(year1, year2)
    return render(request, 'search.html', {'title': title, "books": books})


def good_books(request):
    q = Queries(endpoint, repo_name)
    good_books = q.get_good_books()
    return render(request, 'categories.html', {"title": "Good Books", "books": good_books})


def bad_books(request):
    q = Queries(endpoint, repo_name)
    bad_books = q.get_bad_books()
    return render(request, 'categories.html', {"title": "Bad Books", "books": bad_books})


def popular_books(request):
    q = Queries(endpoint, repo_name)
    books = q.get_popular_books()
    return render(request, 'categories.html', {"title": "Popular Books", "books": books})


def long_books(request):
    q = Queries(endpoint, repo_name)
    books = q.get_long_books()
    return render(request, 'categories.html', {"title": "Long Books", "books": books})


def short_books(request):
    q = Queries(endpoint, repo_name)
    books = q.get_short_books()
    return render(request, 'categories.html', {"title": "Short Books", "books": books})


def seen_books(request):
    q = Queries(endpoint, repo_name)
    books = q.get_seen_books()
    return render(request, 'categories.html', {"title": "Read Books", "books": books})
