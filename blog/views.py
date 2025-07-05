from django.shortcuts import render, get_object_or_404, redirect
from .models import Post


def get_post_list(request):
    posts = Post.objects.all()

    return render(request, 'blog/post_list.html', context={'posts': posts})


def get_post_detail(request, post_id):
    # post = Post.objects.get(id=post_id)
    post = get_object_or_404(Post, id=post_id)

    context = {'post': post}

    return render(request, 'blog/post_detail.html', context)


def create_post(request):
    if request.method == "GET":
        return render(request, 'blog/post_add.html')
    
    if request.method == "POST":
        post = Post.objects.create(title=request.POST.get('title'), text=request.POST.get('text'))

        return redirect('post_detail', post_id=post.id)

def login_view(request):
    if request.method == "GET":
        return render(request, 'blog/login.html')

def update_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if request.method == "GET":
        return render(request, 'blog/post_edit.html', {'post': post})

    if request.method == "POST":
        post.title = request.POST.get('title', post.title)  # Обновляем, если передано
        post.text = request.POST.get('text', post.text)
        post.save()
        return redirect('post_detail', post_id=post.id)