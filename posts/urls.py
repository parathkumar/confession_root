from django.urls import path
from .views import Posts
# from .views import logoutConfirmation

app_name = 'posts'

urlpatterns = [
    path('',Posts.as_view(),name="allposts"),
]