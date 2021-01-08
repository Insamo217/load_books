from django.urls import path
from django.conf import settings
from .save_feed import generateXML

from .views import *

urlpatterns = [
    path('', books_list, name='books_list_url'),
    path('create/', BookCreate.as_view(), name='post_create_url'),
    path('login/', user_login, name='user_login'),
    path('logout/', user_logout, name='user_logout'),
    path('feed/', generateXML, name='generateXML'),
    path('<str:slug>/', books_detail, name='book_detail_url'),

]