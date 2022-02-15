from ast import And, Or
from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.contrib import messages
from reviews.forms import ReviewForm
from .models import Book, Contributor, Review, BookContributor
from .utils import average_rating

from cart.forms import CartAddProductForm


def home_page_view(request):
    return render(request, 'reviews/bookr_landing_page.html')

def bookorder(request,):
    return render(request, 'reviews/comingsoon.html')

def bookorder_view(request,id):
    return render(request, 'reviews/comingsoon.html')


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
    contributor = get_object_or_404(BookContributor, role='AUTHOR',book_id=id)  
    author = Contributor.objects.get(id=contributor.id)
    
    cart_product_form = CartAddProductForm()
    
    
        
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
            messages.success(request, 'Review Created')
            
            
    else:
        review_form = ReviewForm()
    
    context = {
        'post': id,
        'comments': review,
        'new_comment' : new_review,
        'comment_form':review_form,
        "book":book,
        "reviews":review,
        "author":author,
        'product': book,
        'cart_product_form': cart_product_form,
        # "rating":rating,
        # "numberOfReviews" : num_of_reviews
        }

    return render(request, "reviews/book_details.html", context)

def delete_review(request, id):
    review = Review.objects.get(id=id)
    book_id = review.book_id
    if review.author == request.user:
        review.delete()
        messages.warning(request, 'Review Deleted')
        return redirect('/book/')

        
def handler404(request, exception):
    return render(request, '404.html', status=404)

def handler500(request, *args, **argv):
    return render(request, '500.html', status=500)   

    
    

