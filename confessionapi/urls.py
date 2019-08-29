from django.urls import path
from .views import DetailedPost,ListPost
urlpatterns = [
    path('',ListPost.as_view(),name="listpostview"),
    path('<int:pk>',DetailedPost.as_view(),name="detailedview")
]