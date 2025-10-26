from django.urls import path
from . import views
from .views import EmailTokenObtainPairView

from rest_framework_simplejwt.views import (
    
    TokenRefreshView,
    TokenVerifyView
)

 
urlpatterns = [
    path("blogposts/", views.BlogPostListCreate.as_view(), name='blogpost-view-create'),
    path("blogposts/<int:pk>/", views.BlogPostRetrieveUpdateDestroy.as_view(), name='blogpost-view-rud'),
    path("blogposts/search/", views.BlogPostList.as_view(), name="blogpost-view-search"),
    path('api/token', EmailTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify')
]