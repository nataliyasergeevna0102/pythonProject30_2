from django_filters import FilterSet
from .models import Post


class PostFilter(FilterSet):
   class Meta:
       model = Post
       fields = {
           'title_post': ['contains'],
           'author': ['exact'],
           'time_in': ['gt'],
       }


