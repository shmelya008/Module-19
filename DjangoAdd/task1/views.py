from django.shortcuts import render, redirect
from django.http import HttpResponse
from django import forms

from models import Buyer, Game

# Create your views here.


def menu(request):
    title = 'Game Store'
    page_name = 'Main page'
    text = 'Welcome to our store'
    context = {
        'title': title,
        'text': text,
        'page_name': page_name
    }
    return render(request, 'menu.html', context)


def shop(request):
    title = 'Game Store'
    page_name = 'Games'
    text = 'Select a game'
    games = ['Atomic Heart', 'Cyberpunk 2077', 'The Witcher 3']
    context = {
        'title': title,
        'page_name': page_name,
        'text': text,
        'games': games,
    }
    return render(request, 'shop.html', context)


def cart(request):
    title = 'Game Store'
    page_name = 'Cart'
    text = 'Your cart is empty'
    context = {
        'title': title,
        'page_name': page_name,
        'text': text
    }
    return render(request, 'cart.html', context)


class UserRegister(forms.Form):
    username = forms.CharField(max_length=30, label='Введите логин:')
    password = forms.CharField(max_length=8, label='Введите пароль:')
    repeat_password = forms.CharField(max_length=8, label='Повторите пароль:')
    age = forms.CharField(max_length=3, label='Введите свой возраст:')


def sign_up(request):
    users = Buyer.object_buyer.all()
    title = 'Game Store'
    page_name = 'Registration'
    text = ''
    form = UserRegister()
    context = {
        'title': title,
        'text': text,
        'page_name': page_name,
        'form': form
    }

    if request.method == 'POST':
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            info = {}
            context = {
                'error': info,
            }

            ex_user = [i for i in users if i == username]
            if ex_user:
                info['error'] = 'Пользователь уже существует'
                return render(request, 'registration_page.html', context, )

            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
                return render(request, 'registration_page.html', context)

            if int(age) < 18:
                info['error'] = 'Вы должны быть старше 18'
                return render(request, 'registration_page.html', context)

            Buyer.object_buyer.create(username, age)

            print(f'Name: {username}')
            print(f'Password: {password}')
            print(f'Age: {age}')

            return HttpResponse(f'Приветствуем {username}')
    # else:
    #     form = UserRegister()

    return render(request, 'registration_page.html', context)

