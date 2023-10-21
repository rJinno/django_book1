from django.urls import path
from . import views
from .views import FriendList, FriendDetail
# from .views import HelloView

urlpatterns = [
    # path('', HelloView.as_view(), name='index'),
    path('', views.index6, name='index6'),
    path('create', views.create, name='create'),
    path('edit/<int:num>', views.edit, name='edit'),
    path('delete/<int:num>', views.delete, name='delete'),
    path('list', FriendList.as_view()),
    path('detail/<int:pk>', FriendDetail.as_view()),
    path('find', views.find, name='find'),

    # path('form', views.form, name='form'),
    # path('<int:id>/<nickname>/', views.index2, name = 'index2'),
    # path('next', views.next, name='next'),
]
