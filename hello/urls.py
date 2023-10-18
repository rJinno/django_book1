from django.urls import path
from . import views
# from .views import HelloView

urlpatterns = [
    # path('', HelloView.as_view(), name='index'),
    path('', views.index6, name='index6'),
    path('create', views.create, name='create'),
    # path('form', views.form, name='form'),
    # path('<int:id>/<nickname>/', views.index2, name = 'index2'),
    # path('next', views.next, name='next'),
]
