from django.urls import path
from . import views

urlpatterns = [
    path('', views.index4, name='index4'),
    path('form', views.form, name='form'),
    path('<int:id>/<nickname>/', views.index2, name = 'index2'),
    path('next', views.next, name='next'),
]
