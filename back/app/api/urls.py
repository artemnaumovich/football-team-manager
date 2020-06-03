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
    SingleCoachView,
    MatchView,
    SingleMatchView,
)

from .sql_views import (
    Q_1_1View,
    Q_1_2View,
    Q_1_3View,
    Q_1_4View,
    Q_1_5View,
    Q_2_1View,
    Q_2_2View,
    Q_2_3View
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
    path('coach/<int:pk>/', SingleCoachView.as_view()),
    path('match/', MatchView.as_view()),
    path('match/<int:pk>/', SingleMatchView.as_view()),

    path('q_1_1/', Q_1_1View.as_view()),
    path('q_1_2/', Q_1_2View.as_view()),
    path('q_1_3/', Q_1_3View.as_view()),
    path('q_1_4/', Q_1_4View.as_view()),
    path('q_1_5/', Q_1_5View.as_view()),

    path('q_2_1/', Q_2_1View.as_view()),
    path('q_2_2/', Q_2_2View.as_view()),
    path('q_2_3/', Q_2_3View.as_view())
]