from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ReviewForm

# Create your views here.
def rental_review(request):
    # POST 요청 --> 폼 --> THANK YOU
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
            return redirect(reverse("cars:thank_you"))
        else:
            # 유효하지 않은 경우 원래 form 객체를 전달
            return render(request, "cars/rental_review.html", context={"form": form})
    else:
        # GET 요청의 경우 빈 폼을 전달
        return render(request, "cars/rental_review.html", context={"form": ReviewForm()})

def thank_you(request):
    return render(request, "cars/thank_you.html")