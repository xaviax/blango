from django.contrib.auth import get_user_model
from django import template
#from django.utils.html import escape
#from django.utils.safestring import mark_safe
from django.utils.html import format_html
user_model=get_user_model()
register=template.Library()
from blog.models import Post
import logging 
logger = logging.getLogger(__name__)


@register.filter
def author_details(author, current_user):
  
  if not isinstance(author, user_model):

   return ""

  if author == current_user:
    return format_html("<strong>me<strong>")

  if author.first_name and author.last_name:
    name=f"{author.first_name} {author.last_name}"

  else:
    name=f"{author.username}"


  if author.email:

   # prefix=f'<a href = "mailto:{email}">'
   prefix=format_html('<a href="mailto:{}">', author.email)
   suffix=format_html("</a>")

  else:
    prefix=""
    suffix=""    

  return format_html('{}{}{}',prefix,name,suffix)


@register.simple_tag
def row(extra_classes=""):
  return format_html('<div class="row {}">', extra_classes)

@register.simple_tag
def endrow():
  return format_html('</div>')


@register.simple_tag
def column(extra_classes=""):
  return format_html('<div class="col {}"', extra_classes)

@register.simple_tag
def endcolumn():
  return format_html('</div>')

@register.inclusion_tag('blog/post-list.html')
def recent_posts(post):
  five_posts = Post.objects.exclude(pk=post.pk)[:5]
  logger.debug("Loaded %d recent posts for post %d", len(five_posts), post.pk)
  return {"title":"Recent Posts", "posts":five_posts}
