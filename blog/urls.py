from django.urls import path
from .views import (
    BlogListView, 
    BlogDetailView, 
    BlogCreateView,
    BlogUpdateView,
    BlogDeleteView
)

urlpatterns = [
    path("post/new/", BlogCreateView.as_view(), name="post_new"),
    # pk is the same as the automatic field "id" been added by django
    # it means primary key 
    path("post/<int:pk>/", BlogDetailView.as_view(), name="post_detail"), 
    path("post/<int:pk>/edit/", BlogUpdateView.as_view(), name="post_edit"),
    path("post/<int:pk>/delete/", BlogDeleteView.as_view(), name="post_delete"), 
    path("", BlogListView.as_view(), name="home"),
]
