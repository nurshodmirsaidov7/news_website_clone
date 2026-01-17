from django.urls import path
from django.views.generic import TemplateView
# from .views import news_list, news_list_detail
from .views import NewsListView, NewsDetailView, HomePageView, ContactPageView

urlpatterns = [
    path('', HomePageView, name='homepage'),
    path("news/all/", NewsListView.as_view(), name='all_news_list'),
    path("news/<int:pk>/", NewsDetailView.as_view(), name='news_list_detail'),
    path("contact/", ContactPageView.as_view(), name='contact'),
    path("404/", TemplateView.as_view(template_name='news/404.html'), name='page_404'),
]