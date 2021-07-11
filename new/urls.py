from django.contrib import admin
from django.urls import path
from new import views

urlpatterns = [
    path("",views.index, name='new'),
    path("varieties", views.varieties, name='varieties'),
    path("strawberry", views.strawberry, name='strawberry'),
    path("gelato", views.gelato, name='gelato'),
    path("butterscotch", views.butterscotch, name='butterscotch'),
    path("chocolate", views.chocolate, name='butterscotch'),
    path("thankyou", views.thankyou, name='thankyou'),
    path("forbooking", views.forbooking, name='forbooking')

  
]