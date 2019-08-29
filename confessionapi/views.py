from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView
from .models import posts
from .serializers import PostSerializer
from .permissions import IsOwnerOrReadOnly
class ListPost(ListCreateAPIView):
    queryset = posts.objects.all()
    serializer_class = PostSerializer

class DetailedPost(RetrieveUpdateDestroyAPIView):
    queryset = posts.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]