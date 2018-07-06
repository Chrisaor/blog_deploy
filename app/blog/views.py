from django.http import HttpResponse
from django.shortcuts import render, redirect

from blog.models import Post

def about(request):
    return render(request, 'post/about.html')

def post_list(request):
    posts = Post.objects.all()
    context = {
        'posts':posts,
    }
    return render(request, 'post/post_list.html', context)

def post_detail(request,pk):
    post = Post.objects.get(pk=pk)
    context = {
        'post':post,
    }
    return render(request, 'post/post_detail.html', context)

def post_add(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        Post.objects.create(author=request.user, title=title, content=content)
        return redirect('post-list')
    else:
        return render(request, 'post/post_add.html')