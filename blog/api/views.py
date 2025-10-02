from rest_framework import generics 

from blog.api.serializers import *
from blog.models import *
from blog.api.permissions import *


class PostList(generics.ListCreateAPIView):

  permission_class=[AuthorModifyOrReadOnly | IsAdminUserForObject]
  queryset = Post.objects.all()
  serializer_class=PostSerializer
  

class PostDetail(generics.RetrieveUpdateDestroyAPIView):

  queryset=Post.objects.all()
  serializer_class=PostSerializer



