from django.shortcuts import redirect, render
from rest_framework import generics

from .serializers import NewsSerializer

from .forms import NewsForm
from .models import News


class NewsListAPIView(generics.ListAPIView):
    queryset = News.objects.order_by('-date')
    serializer_class = NewsSerializer


def create(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            form.save()
            NewsForm()
    form = NewsForm()

    return render(request, 'medusa_news/news_create.html', {'form': form})
