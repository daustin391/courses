from django.urls import path
from course import views

urlpatterns = [path("", views.index), path("courses", views.create)]
