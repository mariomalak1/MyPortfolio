from django.urls import path
from . import views
urlpatterns = [
    path("", views.MainPage, name="MainPage"),
    # path("create_tag/", views.create_tag, name="create_tag"),
]