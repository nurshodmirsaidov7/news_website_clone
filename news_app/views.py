from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, TemplateView
from django.http import HttpResponse

from .models import News, Category
from .forms import ContactForm
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

def HomePageView(request):
    news = News.published.all()
    categories = Category.objects.all()
    context = {
        'news': news,
        'category': categories
    }

    return render(request, 'news/home.html', context)

# def ContactPageView(request):
#     print(request.POST)
#     form = ContactForm(request.POST or None)
#     print(form)
#     if request.method == 'POST' and form.is_valid():
#         form.save()
#         return HttpResponse("<h2>Thank you for your message. We will get back to you soon.</h2>")

#     context = {
#         'form': form
#     }
#     return render(request, 'news/contact.html', context)

class ContactPageView(TemplateView):
    template_name = 'news/contact.html'

    def get(self, request, *args, **kwargs):
        form = ContactForm()
        context = {
            'form': form
        }

        return render(request, 'news/contact.html', context)
    
    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if request.method == 'POST' and form.is_valid():
            form.save()
            return HttpResponse('<h2>Thank you for your message. We will get back to you soon. </h2>')
        context = {
            'form': form
        }
        return render(request, 'news/contact.html', context)

class NewsListView(ListView):
    model = News
    template_name = 'news/news_list.html'

class NewsDetailView(DetailView):
    model = News
    template_name  = 'news/news_detail.html'
