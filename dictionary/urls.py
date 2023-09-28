from django.urls import path
from .views import home , dictionaryView 

urlpatterns = [
    path('', home , name="home"),
    path('detail/<str:slug>', dictionaryView , name="detail"),

]
