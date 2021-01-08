from django.shortcuts import render, get_object_or_404, redirect
from .models import Books
from .forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View
from .utils import *
from django.contrib.auth.models import User


class BookCreate(LoginRequiredMixin, ObjectCreateMixin, View):
    model_form = BookForm
    template = 'books/book_create_form.html'
    raise_exception = True


def books_list(request):
    title = 'Список книг'
    books = Books.objects.all()
    return render(request, 'books/index.html', context={'books': books, 'title': title})


def books_detail(request, slug):
    book = get_object_or_404(Books, slug__iexact=slug)
    return render(request, 'books/book_detail.html', context={'book': book, 'title': book})


def user_login(request):
    title = 'Авторизация'
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('books_list_url'))
                else:
                    return HttpResponse('User not active')
            else:
                messages.error(request, 'Данные введены неверно!')

    else:
        form = UserLoginForm()

    context = {
        'form': form, 'title': title
    }

    return render(request, 'books/login.html', context)


def user_logout(request):
    logout(request)
    return redirect('books_list_url')




