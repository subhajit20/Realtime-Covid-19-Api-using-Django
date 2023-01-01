from django.urls import path
from .views import GetCovid19data,SearchbyCountryName

urlpatterns = [
    path("s1/", GetCovid19data),
    path("s2/",SearchbyCountryName)
]
