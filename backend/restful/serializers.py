from rest_framework import serializers
from .models import Scraper


class ScraperSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Scraper
        fields = ('tweets_filter', 'reviews_filter')
