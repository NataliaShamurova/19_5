from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Post


def post_list(request):
    post_list = Post.objects.all()

    # Получаем количество постов на странице из параметра запроса, если его нет, берем значение по умолчанию
    page_size = int(request.GET.get('page_size', 5))  # Приводим к int, устанавливаем 5 по умолчанию
    paginator = Paginator(post_list, page_size)

    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)

    return render(request, 'blog/post_list.html', {'posts': posts})

