from rest_framework import generics 

from blog.api.serializers import *
from blog.models import *


class PostList(generics.ListCreateAPIView):

  queryset = Post.objects.all()
  serializer_class=PostSerializer
  

class PostDetail(generics.RetrieveUpdateDestroyAPIView):

  queryset=Post.objects.all()
  serializer_class=PostSerializer



