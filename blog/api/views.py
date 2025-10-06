from rest_framework import generics 

from blog.api.serializers import *
from blog.models import *
from blog.api.permissions import *


class PostList(generics.ListCreateAPIView):

  permission_class=[AuthorModifyOrReadOnly | IsAdminUserForObject]
  queryset = Post.objects.all()
  serializer_class=PostSerializer
  

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
  permission_classes = [AuthorModifyOrReadOnly | IsAdminUserForObject]
  queryset=Post.objects.all()
  serializer_class=PostSerializer


class UserDetail(generics.RetrieveAPIView):
  lookup_field="email"
  queryset=User.objects.all()
  serializer_class=UserSerializer



