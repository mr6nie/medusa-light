from venv import create
from django.urls import path
from . import views

urlpatterns = [
    path('', views.create, name='create'),
    path('news/', views.NewsListAPIView.as_view(), name='news_list')
]
