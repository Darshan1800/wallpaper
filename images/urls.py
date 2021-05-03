from django.urls import path,include
from . import views

app_name = 'images'

urlpatterns = [

    path('<slug:slug>/', views.PostDetailView.as_view()  , name="detail"),
    path('hitcount/', include(('hitcount.urls', 'hitcount'), namespace='hitcount')),
    path('tag/<slug:slug>/',views.tagged,name="tags"),
   
]
