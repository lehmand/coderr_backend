from django_filters.rest_framework import FilterSet, NumberFilter
from reviews_app.models import Review

class ReviewFilter(FilterSet):

    business_user_id = NumberFilter(field_name='business_user_id', lookup_expr='exact')
    reviewer_id = NumberFilter(field_name='reviewer_id', lookup_expr='exact')

    class Meta:
        model = Review
        fields = ['business_user_id', 'reviewer_id']