from django.urls import path
from . import views

urlpatterns = [
    path('', views.index3, name='index3'),
    path('<int:id>/<nickname>/', views.index2, name = 'index2'),
    path('next', views.next, name='next'),
]
