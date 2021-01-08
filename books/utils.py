from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.views.generic import View
from .models import *
from .forms import *


class ObjectCreateMixin:
    title = None
    model_form = None
    template = None

    def get(self, request):
        form = self.model_form()
        title = 'Добавление книги'
        return render(request, self.template,
                      context={'form': form, 'title': title})

    def post(self, request):
        bound_form = self.model_form(request.POST)
        title = 'Добавление книги'
        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj)
        return render(request, self.template,
                      context={'form': bound_form, 'title': title})