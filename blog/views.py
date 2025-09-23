from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment, Tag
from django.utils import timezone
from .forms import *
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_headers
from django.views.decorators.vary import vary_on_cookie
import logging 
# Create your views here.

logger=logging.getLogger(__name__)


def index(request):
  #from django.http import HttpResponse
  #return HttpResponse(str(request.user).encode("ascii"))
  posts=Post.objects.filter(published_at__lte=timezone.now()).select_related("author")
  #Adding a log below 
  logger.debug("Got %d posts.",len(posts))
  return render(request,"blog/index.html",{'posts':posts})



def post_detail(request,slug):
  post = get_object_or_404(Post, slug=slug)

  if request.user.is_active:
    if request.method =="POST":
      comment_form = CommentForm(request.POST)
      
      if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.content_object = post 
        comment.creator = request.user
        comment.save()
        logger.info("Created comment on Post %d for user %s",
        post.pk,request.user)
        return redirect(request.path_info)

    else:
      comment_form=CommentForm()        

  else:
    comment_form = None



  return render(request,"blog/post-detail.html",{'post':post, 'comment_form':comment_form})


def get_ip(request):
  from django.http import HttpResponse
  return HttpResponse(request.META['REMOTE_ADDR'])

  