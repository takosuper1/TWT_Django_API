from django.urls import path
from . import views

url_patterns = [
    path("blogposts/", views.BlogPostListCreate.as_view(), name="blogpost-view-create")
]