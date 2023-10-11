from django.contrib import admin
from django.urls import path
from app.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', CarsView.as_view(), name='home'),
    path('about/<int:pk>', AboutCar.as_view(), name='about'),
    path('create/', CreateCar.as_view(), name='create'),
    path('delete/<int:pk>/', DeletePicture.as_view(), name='delete'),
]