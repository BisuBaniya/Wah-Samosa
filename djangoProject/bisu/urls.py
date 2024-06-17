from django.urls import path
from . import views

#localhost:5000/bisu
#localhost:5000/bisu/order

urlpatterns = [
    path('',views.info,name='info'),
    path('order/',views.order,name='order'),
]

