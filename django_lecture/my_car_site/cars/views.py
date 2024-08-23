from django.shortcuts import render,redirect
from django.urls import reverse
from . import models


# Create your views here.
def list(request):
    return render(request, "cars/list.html", context={'all_cars': models.Car.objects.all()})


def add(request):
    if request.POST:
        brand_name = request.POST['brand']
        production_year = int(request.POST['year'])
        models.Car.objects.create(brand=brand_name,year=production_year)
        # if user submitted new car --> list.html
        return redirect(reverse('cars:list'))
    else:
        return render(request, "cars/add.html")


def delete(request):
    if request.POST:
        # delete the car
        pk = request.POST['pk']
        try:
            models.Car.objects.get(pk=pk).delete()
            return redirect(reverse('cars:list'))
        except:
            print("pk not found!")
            return redirect(reverse('cars:list'))
    else:
        return render(request, "cars/delete.html")
