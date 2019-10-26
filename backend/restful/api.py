from rest_framework import serializers, viewsets
from .models import Scraper


class ScraperSerialiser(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Note
        fields = ('tweets_filter', 'reviews_filter')


class ScraperViewSet(viewsets.ModelViewSet):
    queryset = Scraper.objects.all()
    serializer_class = ScraperSerialiser
