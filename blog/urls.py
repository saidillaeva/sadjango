from django.urls import path
from blog.views import post_view

urlpatterns = [
    path('post/', post_view),
]