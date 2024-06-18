import django_filters
from .models import Post
from django import forms


class PostFilter(django_filters.FilterSet):
    time_in = django_filters.DateFilter(
        widget=forms.DateInput(attrs={'type':'date'}),
        field_name="time_in",
        lookup_expr='date_gre',
        label='Date'
    )

    class Meta:
        model = Post
        fields = {
           'title_post',
           'author'
        }


# from news.filters import PostFilter
#f=PostFilter({'time_in':'5/5/2024','title_post':'testing text', 'author':'Roman'})
#id__in=id_tuple)
#f.errors