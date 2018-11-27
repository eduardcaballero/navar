from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

def index(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'navar/index.html', {'posts': posts})

def lo(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('usuario_detalle', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'navar/login.html', {'form': form})
@login_required
def usuario_detalle(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'navar/usuario.html', {'usuario': post})
@login_required
def registrar(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('usuario_detalle', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'navar/usuario_add.html', {'form': form})
@login_required
def usuario_editar(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('usuario_detalle', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'navar/usuario_editar.html', {'form': form})
@login_required
def usuario_eliminar(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('index')