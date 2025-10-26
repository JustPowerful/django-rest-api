from django.urls import path
from . import views
 
urlpatterns = [
    path("blogposts/", views.BlogPostListCreate.as_view(), name='blogpost-view-create'),
    path("blogposts/<int:pk>/", views.BlogPostRetrieveUpdateDestroy.as_view(), name='blogpost-view-rud'),
    path("blogposts/search/", views.BlogPostList.as_view(), name="blogpost-view-search")
]