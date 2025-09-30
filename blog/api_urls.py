from django.urls import path, include 
from blog import api_views  
from rest_framework.urlpatterns import format_suffix_patterns



urlpatterns=[
  path("posts",api_views.post_list,name="post_list"),
  path("posts/<int:pk>/",api_views.post_detail, name="post_detail"),

]

urlpatterns= format_suffix_patterns(urlpatterns)
