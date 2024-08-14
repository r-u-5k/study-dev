from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

articles = {
    "sports": "Sports Page",
    "finance": "Finance Page",
    "politics": "Politics Page"
}


def news_view(request, topic):
    try:
        return HttpResponse(articles[topic])
    except:
        raise Http404("404 GENERIC ERROR")


def num_page_view(request, num_page):
    topics_list = list(articles.keys())
    topic = topics_list[num_page]
    return HttpResponseRedirect(reverse('news_view', args=[topic]))
