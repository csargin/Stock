from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.home, name ="home"),
    path('about.html', views.about, name ="about"),
    path('search.html', views.search, name ="search"),
    path('add_stock.html', views.add_stock, name ="add_stock"),
    path('delete/<stock_name>', views.delete, name ="delete"),
    path('analysis/<stock_name>', views.analysis, name ="analysis"),
    path('admin/', admin.site.urls),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)