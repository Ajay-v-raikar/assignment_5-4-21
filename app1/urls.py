from django.contrib import admin
from django.urls import path
from app1 import views
urlpatterns = [
    path('',views.index,name="index"),
    path('sample',views.sample,name="sample"),
    path('sample_app1',views.sample_view,name="sample_view"),
]