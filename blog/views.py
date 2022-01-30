from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from blog.models import Post, Comment
from blog.forms import EmailPostForm, NewCommentForm
from django.core.mail import send_mail


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

    context = {
        'page': page,
        'posts': posts,
        'paginator': paginator
    }

    return render(request, 'blog/post_list.html', context)


def post_detail(request, post):
    post = get_object_or_404(Post, slug=post, status='published')

    #post-comment-logics
    comments = post.comments.filter(active=True)
    new_comment = None
    if request.method == 'POST':
        comment_form = NewCommentForm(data = request.POST)
        if comment_form.is_valid():
            post = post.id
            name = request.POST.get('name')
            comment_body = request.POST.get('body')
            new_comment = Comment.objects.create(post=post, name=name, body=comment_body)
            new_comment.save()
            

            new_comment.post = post
            new_comment = comment_form.save()
    else:
        comment_form = NewCommentForm()

    context = {
        'post': post,
        'comments': comments,
        'new_comment' : new_comment,
        'comment_form':comment_form
        }

    return render(request, 'blog/post_detail.html', context)


def tailwind(request):
    return render(request, 'blog/tailwind.html')


def post_share(request,post):
    post_obj = get_object_or_404(Post, slug=post, status='published')
    '''filtering post by unique slug fiels'''
    send_message = False
    recipients = ''
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
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
        form = EmailPostForm()

    context = {
        'form': form,
        'title': post_obj.title,
        'send': send_message,
        'recipients': recipients
    }
    return render(request, 'blog/share.html', context)

 
