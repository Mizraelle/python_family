from django.urls import path, re_path
from . import views

urlpatterns = [
    path('hello/', views.hello),
    path('form/', views.form),
    path('add_like/', views.add_like),
    re_path(r'(?P<slug>[^/]+)/$', views.onevideo),
]