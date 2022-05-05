from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("blogs", views.blogs, name="blogs"),
    # path("<str:title>", views.blog1, name="blog1"),
    path("blog1/<str:title>", views.blog1, name="blog1"),
    path("contact", views.contact, name="contact"),
    path("categories/<str:title>", views.categories, name="categories"),
    path("search", views.search, name="search")
]
