from django import forms
from .models import *
from django.core.exceptions import ValidationError


class BookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = ['title', 'description', 'price', 'photo']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),

        }

        def clean_slug(self):
            new_slug = self.cleaned_data['slug'].lower()

            if new_slug == 'create':
                raise ValidationError('Slug не может быть создан')
            return new_slug


class UserLoginForm(forms.Form):
    username = forms.CharField(label="", widget=forms.TextInput
                               (attrs={'placeholder': 'Введите имя здесь...'}))
    password = forms.CharField(label="", widget=forms.PasswordInput
                                (attrs={'placeholder': 'Введите пароль здесь...'}))