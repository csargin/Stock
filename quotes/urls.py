from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name ="home"),
    path('about.html', views.about, name ="about"),
    path('search.html', views.search, name ="search"),
    path('add_stock.html', views.add_stock, name ="add_stock"),
    path('delete_stock.html>', views.delete_stock, name ="delete_stock"),

]