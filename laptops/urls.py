from django.urls import path
from laptops.views import LaptopsAPIView


app_name = 'laptops'

urlpatterns = [
     path('laptop/', LaptopsAPIView.as_view(), name='laptop'),
     path('laptops/<int:pk>', LaptopsAPIView.as_view(), name='laptops'),

]