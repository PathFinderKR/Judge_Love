from django.urls import path
from . import views

urlpatterns = [
    path('', views.story_view, name='story'),
    path('result/', views.result_view, name='result'),
    path('appeal/', views.appeal_view, name='appeal'),
]
