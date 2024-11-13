from django.shortcuts import render
from .forms import UserRegister
from .models import *

menu = [
    {'title': 'Товары', 'url_name': 'product'},
    {'title': 'Корзина', 'url_name': 'card'},
]


def home_page(request):
    data = {
        'title': 'Главная страница',
        'menu': menu
    }
    return render(request, 'task1/platform.html', context=data)


def shop_page(request):
    games = Game.objects.all()
    data_db = {
        'title': 'Магазин',
        'menu': menu,
        'products': games,
    }

    return render(request, 'task1/product.html', context=data_db)


def cart_page(request):
    context = {
        'title': 'Корзина',
        'content': "Извините, Ваша корзина пуста",
        'menu': menu,
    }

    return render(request, 'task1/cart.html', context=context)


# Псевдо-список существующих пользователей

#users = ['user1', 'user2', 'admin']


def sign_up_by_django(request):
    info = ''
    #Users = Buyer.objects.all()

    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            # Проверка на существование пользователя в базе данных
            if Buyer.objects.filter(name=username).exists():
                info = "Ошибка: пользователь уже существует."
            elif password != repeat_password:
                info = "Ошибка: пароли не совпадают."
            elif age < 18:
                info = "Ошибка: возраст должен быть не менее 18 лет."
            else:

                # Создание нового пользователя

                Buyer.objects.create(name=username, balance=500.0, age=age)
                info = f"Приветствуем, {username}!"

    else:
        form = UserRegister()

    context = {'form': form, 'info': info}
    return render(request, 'task1/registration_page.html', context)



def sign_up_by_html(request):
    info = ''  # Пустая строка для информации

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        repeat_password = request.POST.get('repeat_password')
        age = request.POST.get('age')

        # Проверка условий
        if username in users:
            info = "Ошибка: пользователь уже существует."
        elif password != repeat_password:
            info = "Ошибка: пароли не совпадают."
        elif int(age) < 18:  # Приводим к int для проверки возраста
            info = "Ошибка: возраст должен быть не менее 18 лет."
        else:
            users.append(username)  # Добавление нового пользователя в список
            info = f"Приветствуем, {username}!"  # Успешное сообщение

    context = {'info': info}  # Передаем информацию в шаблон
    return render(request, 'task1/registration_page.html', context)  # Отображение шаблона

