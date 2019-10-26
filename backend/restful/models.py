from django.db import models
#from django.utils import timezone
# from django.core.validators import MaxValueValidator,


class Scraper(models.Model):
    tweets_filter = models.CharField(max_length=100)
    reviews_filter = models.IntegerField(default=0)

    def __str__(self):
        return "{} - {}".format(self.tweets_filter, self.reviews_filter)

        
