from django.shortcuts import render
from django.http import HttpResponse
from .models import Post, Category
from .forms import commentForm

# Create your views here.


def homepage(request):

    posts = Post.objects.all()
    categories = Category.objects.all()
    header = 'This is my blog'

    return render(request, 'index.html', {
        'titles': posts,
        'header': header,
        'categories': categories})


def singlepost(request, post_id):

    post = Post.objects.get(id=post_id)
    form = commentForm()
    comments = post.comments.all()
    if request.method == 'POST':
        form = commentForm(request.POST)

        if form.is_valid:
            comment = form.save(commit=False)
            comment.post = post
            comment.save()


    return render(request, 'singlepost.html', {
        'post':post,
        'comments':comments,
        'form':form})


def about(request):

    return render(request, 'about.html', {})
