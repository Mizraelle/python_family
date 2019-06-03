from django.urls import path
from . import views


urlpatterns = [
    path(r'in/', views.login),
    path(r'out/', views.out)
]