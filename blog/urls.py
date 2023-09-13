from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_page, name="home-page"),
    path("posts/", views.posts_page, name="post-page"),
    path("posts/<slug:post>", views.post_details, name="post-details")
]