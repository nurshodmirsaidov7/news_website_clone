from django.urls import path
# from .views import news_list, news_list_detail
from .views import NewsListView, NewsDetailView

urlpatterns = [
    path("all/", NewsListView.as_view(), name='all_news_list'),
    path("<int:pk>/", NewsDetailView.as_view(), name='news_list_detail')
]