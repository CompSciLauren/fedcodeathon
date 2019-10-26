from django.urls import path
from .views import ListScraperResultsView


urlpatterns = [
    path('results/', ListScraperResultsView.as_view(), name="results")
]
