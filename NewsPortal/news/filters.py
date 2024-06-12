import django_filters
from .models import Post
from django import forms

class DateFilter:
    pass


class PostFilter(django_filters.FilterSet):
    time_in = DateFilter(
        widget = forms.DateInput(attrs={'type':'date'}),
        field_name = "time_in",
        lookup_expr = 'date_gre'
    )

    class Meta:
        model = Post
        fields = {
           'title_post': ['icontains'],
           'author': ['iexact'],
        }


