from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    get_object_or_404
)
from .models import (
    Country,
    City,
    Stadium,
    Team,
    Person,
    Player,
    Coach
)
from .serializers import (
    CountrySerializer,
    CitySerializer,
    StadiumSerializer,
    TeamSerializer,
    PersonSerializer,
    PlayerSerializer,
    CoachSerializer
)
from django.db import IntegrityError
from rest_framework import serializers


class CountryView(ListCreateAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class SingleCountryView(RetrieveUpdateDestroyAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CityView(ListCreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

    def perform_create(self, serializer):
        country = get_object_or_404(Country, id=self.request.data.get('country_id'))
        return serializer.save(country=country)


class SingleCityView(RetrieveUpdateDestroyAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

    def perform_update(self, serializer):
        country = get_object_or_404(Country, id=self.request.data.get('country_id'))
        return serializer.save(country=country)


class StadiumView(ListCreateAPIView):
    queryset = Stadium.objects.all()
    serializer_class = StadiumSerializer

    def perform_create(self, serializer):
        try:
            city = get_object_or_404(City, id=self.request.data.get('city_id'))
            return serializer.save(city=city)
        except IntegrityError as integrityError:
            raise serializers.ValidationError({"city, address": ["stadium with this city and address already exists."]})


class SingleStadiumView(RetrieveUpdateDestroyAPIView):
    queryset = Stadium.objects.all()
    serializer_class = StadiumSerializer

    def perform_update(self, serializer):
        try:
            city = get_object_or_404(City, id=self.request.data.get('city_id'))
            return serializer.save(city=city)
        except IntegrityError as integrityError:
            raise serializers.ValidationError({"city, address": ["stadium with this city and address already exists."]})


class TeamView(ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    def perform_create(self, serializer):
        city = get_object_or_404(City, id=self.request.data.get('city_id'))
        return serializer.save(city=city)


class SingleTeamView(RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    def perform_update(self, serializer):
        city = get_object_or_404(City, id=self.request.data.get('city_id'))
        return serializer.save(city=city)


class PersonView(ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def perform_create(self, serializer):
        country_of_birth = get_object_or_404(Country, id=self.request.data.get('country_of_birth_id'))
        return serializer.save(country_of_birth=country_of_birth)


class SinglePersonView(RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

    def perform_update(self, serializer):
        country_of_birth = get_object_or_404(Country, id=self.request.data.get('country_of_birth_id'))
        return serializer.save(country_of_birth=country_of_birth)


class PlayerView(ListCreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

    def perform_create(self, serializer):
        try:
            person = get_object_or_404(Person, id=self.request.data.get('person_id'))
            if not self.request.data.get('team_id'):
                team = None
            else:
                team = get_object_or_404(Team, id=self.request.data.get('team_id'))
            return serializer.save(person=person, team=team)
        except IntegrityError as integrityError:
            raise serializers.ValidationError({"person": ["player with this person already exists."]})


class SinglePlayerView(RetrieveUpdateDestroyAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer

    def perform_update(self, serializer):
        try:
            person = get_object_or_404(Person, id=self.request.data.get('person_id'))
            if not self.request.data.get('team_id'):
                team = None
            else:
                team = get_object_or_404(Team, id=self.request.data.get('team_id'))
            return serializer.save(person=person, team=team)
        except IntegrityError as integrityError:
            raise serializers.ValidationError({"person": ["player with this person already exists."]})


class CoachView(ListCreateAPIView):
    queryset = Coach.objects.all()
    serializer_class = CoachSerializer

    def perform_create(self, serializer):
        try:
            person = get_object_or_404(Person, id=self.request.data.get('person_id'))
            if not self.request.data.get('team_id'):
                team = None
            else:
                team = get_object_or_404(Team, id=self.request.data.get('team_id'))
            return serializer.save(person=person, team=team)
        except IntegrityError as integrityError:
            error = str(integrityError.args[0])
            if error.endswith('person_id'):
                raise serializers.ValidationError({"person": ["coach with this person already exists."]})
            elif error.endswith('team_id'):
                raise serializers.ValidationError({"team": ["coach with this team already exists."]})


class SingleCoachView(RetrieveUpdateDestroyAPIView):
    queryset = Coach.objects.all()
    serializer_class = CoachSerializer

    def perform_update(self, serializer):
        try:
            person = get_object_or_404(Person, id=self.request.data.get('person_id'))
            if not self.request.data.get('team_id'):
                team = None
            else:
                team = get_object_or_404(Team, id=self.request.data.get('team_id'))
            return serializer.save(person=person, team=team)
        except IntegrityError as integrityError:
            error = str(integrityError.args[0])
            if error.endswith('person_id'):
                raise serializers.ValidationError({"person": ["coach with this person already exists."]})
            elif error.endswith('team_id'):
                raise serializers.ValidationError({"team": ["coach with this team already exists."]})
