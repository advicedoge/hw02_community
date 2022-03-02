from django.shortcuts import render, get_object_or_404

from .models import Post, Group

DISPLAY_LIMIT = 10


def index(request):
    posts = Post.objects.order_by('-pub_date')[:DISPLAY_LIMIT]
    template = 'posts/index.html'
    context = {
        'posts': posts,
        'title': 'Yatube Главная страница',
        'text': 'Это главная страница проекта Yatube'
    }

    return render(request, template, context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = posts = group.posts.all().order_by('-pub_date')[:DISPLAY_LIMIT]
    context = {
        'group': group,
        'posts': posts,
        'title': 'Страница сообщества Yatube',
    }
    return render(request, 'posts/group_list.html', context)
