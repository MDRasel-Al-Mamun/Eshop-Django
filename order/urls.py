from django.urls import path
from . import views

urlpatterns = [
    path('addtoshopcart/<int:id>', views.addtoshopcart, name='addtoshopcart'),
    path('deleteshopcart/<int:id>', views.deleteshopcart, name='deleteshopcart'),
    path('orderproduct/', views.orderproduct, name='orderproduct'),
]
