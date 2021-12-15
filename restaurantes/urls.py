from django.urls import path
from .views import restaurants_api_view, restaurant_detail_view
from restaurantes import views

urlpatterns = [
    path('',views.restaurants_api_view,name="restaurant_list_api"),
    path('detail/<str:pk>/',restaurant_detail_view,name='restaurant_detail_api_view'),
]