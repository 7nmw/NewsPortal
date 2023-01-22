from django_filters import FilterSet, DateFilter
from django.forms import DateInput
from .models import Post




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
