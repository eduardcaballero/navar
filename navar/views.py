from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm

def index(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'navar/index.html', {'posts': posts})

def login(request):
    form = PostForm()
    return render(request, 'navar/login.html', {'form': form})

def perfil_detalle(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'navar/perfil.html', {'perfil': post})