from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    TemplateView,
    FormView,
    CreateView,
    ListView,
    DetailView,
    UpdateView,
    DeleteView
)
from .forms import ContactForm
from .models import Teacher


# Create your views here.
class HomeView(TemplateView):
    template_name = "classroom/home.html"


class ThankYouView(TemplateView):
    template_name = "classroom/thank_you.html"


class ContactFormView(FormView):
    form_class = ContactForm
    template_name = "classroom/contact.html"
    success_url = reverse_lazy("classroom:thank_you")

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class TeacherCreateView(CreateView):
    model = Teacher  # teacher_form.html과 연결됨
    fields = "__all__"  # ["first_name", "last_name", "subject"]
    success_url = reverse_lazy("classroom:thank_you")

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)


class TeacherListView(ListView):
    model = Teacher  # teacher_list.html과 연결됨
    queryset = Teacher.objects.order_by("first_name")
    context_object_name = "teacher_list"  # html 파일 내부의 for문 안에 들어가는 객체 이름 지정 (디폴트: object_list)


class TeacherDetailView(DetailView):
    model = Teacher  # teacher_detail.html과 연결됨
    # PK --> {{teacher}}


class TeacherUpdateView(UpdateView):
    model = Teacher
    fields = "__all__"
    success_url = reverse_lazy("classroom:list_teacher")


class TeacherDeleteView(DeleteView):
    model = Teacher # teacher_confirm_delete.html과 연결됨
    success_url = reverse_lazy("classroom:list_teacher")