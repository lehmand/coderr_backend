from reviews_app.models import Review
from rest_framework.response import Response
from offers_app.models import Offer
from django.db.models import Avg
from rest_framework.views import APIView
from rest_framework import status


class BaseInfoView(APIView):

    def get(self, request):

        review_count = Review.objects.count()
        average_rating = Review.objects.aggregate(avg_rating=Avg('rating'))['avg_rating']
        average_rating = round(average_rating, 1) if average_rating is not None else 0.0
        business_profile_count = Offer.objects.values('user').distinct().count()
        offer_count = Offer.objects.count()

        data = {
            'review_count': review_count,
            'average_rating': average_rating,
            'business_profile_count': business_profile_count,
            'offer_count': offer_count
        }

        return Response(data, status=status.HTTP_200_OK)

        