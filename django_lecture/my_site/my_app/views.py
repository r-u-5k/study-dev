from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

# Create your views here.
def simple_view(request):
    return render(request,'my_app/example.html') # .html