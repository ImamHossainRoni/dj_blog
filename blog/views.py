from django.shortcuts import render, get_object_or_404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.generic import ListView

# Create your views here.


def post_list(request):
    object_list = Post.published.all()
    page = request.GET.get('page')
    paginator = Paginator(object_list, 3)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'list.html', {'posts': posts})


def post_details(request, pk):
    post = get_object_or_404(Post, id=pk)
    return render(request, 'details.html', {'post': post})
