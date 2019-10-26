from django.db import models
#from django.utils import timezone
# from django.core.validators import MaxValueValidator,


class Scraper(models.Model):
    business_type = models.CharField(max_length=100, null=True)
    longitude = models.CharField(max_length=100, null=True)
    latitude = models.CharField(max_length=100, null=True)
    city = models.CharField(max_length=100, null=True)

    # def __str__(self):
    #    return "{} - {}".format(self.tweets_filter, self.reviews_filter)
