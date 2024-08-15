from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse


# Create your views here.
def example_view(request):
    # my_app/templates/my_app/example.html
    return render(request, "my_app/example.html")


def variable_view(request):
    my_var = {
        "first_name": "RosaLind",
        "last_name": "franKlin",
        "some_list": [1, 2, 3],
        "some_dict": {"inside_key": "inside_value"},
    }
    return render(request, "my_app/variable.html", context=my_var)
