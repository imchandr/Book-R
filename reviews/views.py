from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Book, Review
from .utils import average_rating


def welcome_view(request):
    return render(request, 'reviews/base.html')


def booklist_view(request):
    books = Book.objects.all()
    book_list = []

    for book in books:
        reviews = book.review_set.all()
        if reviews:
            rating = average_rating([review.rating for review in reviews])
            num_of_reviews = len(reviews)
        else:
            rating = None
            num_of_reviews = 0

        book_list.append({
            "book": book,
            "book_rating": rating,
            "number_of_reviews": num_of_reviews,
        })

        context = {
            "book_list": book_list,
        }
       

    return render(request, "reviews/books_list.html", context)

def bookdetails_view(request, id):
    book = get_object_or_404(Book, id=id)
    reviews = book.review_set.all()
    num_of_reviews = len(reviews)
    rating = average_rating([review.rating for review in reviews])

    print (book)

    context = {
        "book":book,
        "reviews":reviews,
        "rating":rating,
        "numberOfReviews" : num_of_reviews
    }

    return render(request, "reviews/book_details.html", context)