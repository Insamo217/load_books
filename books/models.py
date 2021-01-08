from django.shortcuts import reverse
from django.db import models
from django.utils.text import slugify
from time import time


def gen_slug(s):
    new_slug = slugify(s, allow_unicode=False)
    return new_slug + str(int(time()))


class Books(models.Model):
    title = models.CharField('Название книги', max_length=150, db_index=True)
    slug = models.SlugField(max_length=150, blank=True, unique=True)
    description = models.TextField('Описание', blank=True, db_index=True)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    photo = models.ImageField('Фото', default='download.png')

    def get_absolute_url(self):
        return reverse('book_detail_url', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'