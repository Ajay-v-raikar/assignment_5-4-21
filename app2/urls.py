from django.contrib import admin
from django.urls import path
from app2 import views
urlpatterns = [
    path('',views.index,name="index"),
    path('sample',views.sample,name="sample"),
    path('sample_app2',views.sample_view,name="sample_view"),
]