from django.shortcuts import render, get_object_or_404
from .models import News, Category
from django.views.generic import ListView, DetailView
# Create your views here.

# def news_list(request):
#     news_list = News.published.all()
#     context = {
#         'news_list': news_list
#     }

#     return render(request, 'news/news_list.html', context)

# def news_list_detail(request, id):
#     news = get_object_or_404(News, id=id, status=News.Status.Published)
#     context = {
#         'news': news
#     }

#     return render(request, 'news/news_detail.html', context)

class NewsListView(ListView):
    model = News
    template_name = 'news/news_list.html'

class NewsDetailView(DetailView):
    model = News
    template_name  = 'news/news_detail.html'
