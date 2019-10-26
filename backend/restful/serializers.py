from rest_framework import serializers
from .models import Scraper


class ScraperSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Scraper
        fields = ('business_type', 'latitude', 'longitude', 'city',)
