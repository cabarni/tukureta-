from django.urls import path
from .views import registfunc, loginfunc, mainfunc, logoutfunc, detailfunc, goodfunc, readfunc, EatCreate, viewfunc

urlpatterns = [
    path('regist/', registfunc, name="regist"),
    path('login/', loginfunc, name="login"),
    path('', mainfunc, name="main"),
    path('logout/', logoutfunc, name="logout"),
    path('detail/<int:pk>', detailfunc, name='detail'),
    path('good/<int:pk>', goodfunc, name="good"),
    path('read/<int:pk>', readfunc, name="read"),
    path('create/', EatCreate.as_view(), name='create'),
    path('view/', viewfunc, name="view"),
]