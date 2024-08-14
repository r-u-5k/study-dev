from django.urls import path
from . import views

urlpatterns = [
    path('<int:num_page>/', views.num_page_view, name='num_page_view'),
    path('<str:topic>/', views.news_view, name='news_view'),
]
