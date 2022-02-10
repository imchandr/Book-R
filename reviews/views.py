from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from reviews.forms import ReviewForm
from .models import Book, Contributor, Review, BookContributor
from .utils import average_rating


def home_page_view(request):
    return render(request, 'reviews/test.html')


def booklist_view(request):
    books = Book.objects.all()
    contributors = BookContributor.objects.filter(role='AUTHOR')
    
    context = {
        "book_list": books,
        "contributors":contributors
               
    }
       

    return render(request, "reviews/books_list.html", context)

def bookdetails_view(request, id):
    book = get_object_or_404(Book, id=id)
    contributor = BookContributor.objects.get(role='AUTHOR',book_id=id)
    author = Contributor.objects.get(id=contributor.id)
    # reviews = book.review_set.all()
    # num_of_reviews = len(reviews)
    # rating = average_rating([review.rating for review in reviews])

    review = book.review.filter(active=True)
    new_review = None
    if request.method == 'POST':
        review_form = ReviewForm(data=request.POST)
        if review_form.is_valid():
           
            new_review = review_form.save(commit=False)
            new_review.author = request.user
            new_review.book_id = book.id
            new_review.save()
            
            
    else:
        review_form = ReviewForm()
    
    context = {
        'post': id,
        'comments': review,
        'new_comment' : new_review,
        'comment_form':review_form,
        "book":book,
        "reviews":review,
        "author":author
        # "rating":rating,
        # "numberOfReviews" : num_of_reviews
        }

    return render(request, "reviews/book_details.html", context)

# def add_review_view(request, id):
#     form = AddReviewForm()
#     context ={
#         "form": form,
#     }
#     if request.method == "POST":
#         form = AddReviewForm(request.POST)
#         if form.is_valid():
            
#             content = form.cleaned_data["review_content"]
#             rating = form.cleaned_data["rating"]

#             print("\n",content,rating)
    

#     return render(request, "reviews/add_review.html", context)

