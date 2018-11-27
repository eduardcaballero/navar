from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect

def index(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'navar/index.html', {'posts': posts})

def login(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('perfil_detalle', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'navar/login.html', {'form': form})

def perfil_detalle(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'navar/perfil.html', {'perfil': post})

def registrar(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('perfil_detalle', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'navar/perfil_editar.html', {'form': form})

def perfil_editar(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('perfil_detalle', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'navar/perfil_editar.html', {'form': form})
# def post_new(request):
#     if request.method == "POST":
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.published_date = timezone.now()
#             post.save()
#             return redirect('blog.views.post_detail', pk=post.pk)
#     else:
#         form = PostForm()
#     return render(request, 'blog/post_edit.html', {'form': form})