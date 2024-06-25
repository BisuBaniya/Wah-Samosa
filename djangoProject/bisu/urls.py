from django.urls import path # type: ignore
from . import views # type: ignore

#localhost:5000/bisu
#localhost:5000/bisu/order

urlpatterns = [
    path('',views.info,name='info'),
    path('samosa_stores/',views.samosa_view_store,name="samosa_stores"),
    path('<int:samosa_id>/',views.samosa_detail,name='samosa_detail'),
]

