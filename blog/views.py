
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blog.models import Post, Comment
from reviews.models import Book
from blog.forms import SharePostForm, CommentForm, NewPostForm, PostSearchForm
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.views.generic import CreateView,UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.files.storage import FileSystemStorage
from django.contrib.postgres.search import SearchVector


class PostCreate(LoginRequiredMixin,CreateView):
    model = Post
    form_class = NewPostForm
    success_url = reverse_lazy('blog:post_list')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(PostCreate, self).form_valid(form)
    
    def upload(request):
        if request.method == 'POST' and request.FILES['image']:
            upload = request.FILES['img']
            fss = FileSystemStorage()
            file = fss.save(upload.name, upload)
            file_url = fss.url(file)
            return HttpResponse('sucess')
        return HttpResponse('somthing wrong has happen')

class PostUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = NewPostForm
    success_url = reverse_lazy('blog:post_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(PostUpdate, self).form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class PostDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('blog:post_list')

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

class CommentDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    success_url = reverse_lazy('blog:post_list') 
    
    def test_func(self):
        comment = self.get_object()
        if self.request.user == comment.name:
            return True
        return False
    
    
def post_list(request):
    object_list = Post.objects.all()
    paginator = Paginator(object_list, 3)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        '''when page isnt a number then show 1st page'''
        posts = paginator.page(1)
    except EmptyPage:
        '''when page num is out of range show the last page'''
        posts = paginator.page(paginator.num_pages)

    form = PostSearchForm()
    context = {
        'page': page,
        'posts': posts,
        'paginator': paginator,
        'form' : form
        
    }

    return render(request, 'blog/post_list.html', context)


def post_detail(request, post):
    post = get_object_or_404(Post, slug=post, status='published')

    
    comments = post.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
           
            new_comment = comment_form.save(commit=False)
            new_comment.name = request.user
            new_comment.post = post
            new_comment.save()
            
            
    else:
        comment_form = CommentForm()
    
    context = {
        'post': post,
        'comments': comments,
        'new_comment' : new_comment,
        'comment_form':comment_form
        }

    return render(request, 'blog/post_detail.html', context)

def post_search(request):
    form = PostSearchForm()
    query = None
    results = []
    if 'query' in request.GET:
        form = PostSearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Post.published.annotate(
                search=SearchVector('title', 'body'),
            ).filter(search=query)  
            # Book.objects.filter().annotate(search=SearchVector('title','description','genre','contributors'))
    return render(request,
                  'blog/search_result.html',
                  {'form': form,
                   'query': query,
                   'results': results})

def tailwind(request):
    return render(request, 'blog/tailwind.html')


def post_share(request,post):
    post_obj = get_object_or_404(Post, slug=post, status='published')
    '''filtering post by unique slug fiels'''
    send_message = False
    recipients = ''
    if request.method == 'POST':
        form = SharePostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data

            post_url = request.build_absolute_uri(post_obj.get_absolute_url())
            title = post_obj.title
            sender = 'admin@bookrApp.com'
            recipients = [cd['to']]
            subject = f"read recommendation from {cd['name']}"
            message = f" Hi, Found a good read for you that is:  " + title + " at " + post_url
            send_mail(subject, message, sender, recipients)

            send_message = True

    else:
        form = SharePostForm()

    context = {
        'form': form,
        'title': post_obj.title,
        'send': send_message,
        'recipients': recipients
    }
    return render(request, 'blog/share.html', context)

def handler404(request, exception):
    return render(request, '404.html', status=404)

def handler500(request, *args, **argv):
    return render(request, '500.html', status=500)
