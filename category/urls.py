from django.urls import path,include
from . import views

app_name = 'category'

urlpatterns = [

    path('',views.category_list   , name="category"),
    path('<slug:slug>/',views.category   , name="catlist"),
    
]
