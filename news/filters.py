from django_filters import FilterSet, DateFilter
from django.forms import DateInput
from .models import Post, PostCategory
import django_filters



class PostFilter(FilterSet):

    datetime_post = DateFilter(
        lookup_expr=('lt'),
        widget=DateInput(attrs={'placeholder': 'Select a date', 'type': 'date'}),
        label='Date',
    )

    class Meta:
        model = Post
        fields = {
            'header': ['icontains'],
            'category_post': ['exact'],
        }


class PostCategoryFilter(FilterSet):
    class Meta:
        model = PostCategory
        fields = ['category']