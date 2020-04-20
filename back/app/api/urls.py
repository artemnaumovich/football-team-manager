from django.urls import path

from .views import (
    CountryView,
    SingleCountryView,
    CityView,
    SingleCityView,
    StadiumView,
    SingleStadiumView,
    TeamView,
    SingleTeamView,
    PersonView,
    SinglePersonView,
    PlayerView,
    SinglePlayerView,
    CoachView,
    SingleCoachView
)


app_name = "api"

urlpatterns = [
    path('country/', CountryView.as_view()),
    path('country/<int:pk>/', SingleCountryView.as_view()),
    path('city/', CityView.as_view()),
    path('city/<int:pk>/', SingleCityView.as_view()),
    path('stadium/', StadiumView.as_view()),
    path('stadium/<int:pk>/', SingleStadiumView.as_view()),
    path('team/', TeamView.as_view()),
    path('team/<int:pk>/', SingleTeamView.as_view()),
    path('person/', PersonView.as_view()),
    path('person/<int:pk>/', SinglePersonView.as_view()),
    path('player/', PlayerView.as_view()),
    path('player/<int:pk>/', SinglePlayerView.as_view()),
    path('coach/', CoachView.as_view()),
    path('coach/<int:pk>/', SingleCoachView.as_view())
]