from django.urls import path, include 
from blog import api_views  

urlpatterns=[
  path("posts/",api_views.post_list,name="post_list"),
  path("posts/<int:pk>/",api_views.post_detail, name="post_detail"),

]