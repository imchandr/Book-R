from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from reviews.forms import AddReviewForm
from .models import Book, Review, BookContributor
from .utils import average_rating


def home_page_view(request):
    return render(request, 'reviews/test.html')


def booklist_view(request):
    books = Book.objects.all()
    contributors = BookContributor.objects.all()
    book_list = []
    
    
        

    for book in books:
        reviews = book.review_set.all()
        if reviews:
            rating = average_rating([review.rating for review in reviews])
            num_of_reviews = len(reviews)
        else:
            rating = None
            num_of_reviews = 0

        # book_author = 
        release_date = book.publication_date

        book_list.append({
            "book": book,
            "book_rating": rating,
            "number_of_reviews": num_of_reviews,
            # "author":book_author,
            "release_date":release_date,
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

    

    context = {
        "book":book,
        "reviews":reviews,
        "rating":rating,
        "numberOfReviews" : num_of_reviews
    }

    return render(request, "reviews/book_details.html", context)

def add_review_view(request, id):
    form = AddReviewForm()
    context ={
        "form": form,
    }
    if request.method == "POST":
        form = AddReviewForm(request.POST)
        if form.is_valid():
            
            content = form.cleaned_data["review_content"]
            rating = form.cleaned_data["rating"]

            print("\n",content,rating)
    

    return render(request, "reviews/add_review.html", context)

