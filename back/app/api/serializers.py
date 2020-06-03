from rest_framework import serializers
from .models import (
    Country,
    City,
    Stadium,
    Team,
    Person,
    Player,
    Coach,
    Match
)
import datetime

class CitySerializer(serializers.ModelSerializer):
    country_id = serializers.IntegerField()
    stadiums = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    teams = serializers.PrimaryKeyRelatedField(read_only=True, many=True)

    class Meta:
        model = City
        fields = ('id',
                  'name',
                  'country_id',
                  'stadiums',
                  'teams')


class CountrySerializer(serializers.ModelSerializer):
    cities = serializers.PrimaryKeyRelatedField(read_only=True, many=True)

    class Meta:
        model = Country
        fields = ('id',
                  'name',
                  'cities')


class StadiumSerializer(serializers.ModelSerializer):
    city_id = serializers.IntegerField()
    capacity = serializers.IntegerField(min_value=0)
    year_of_opening = serializers.IntegerField(min_value=0)

    class Meta:
        model = Stadium
        fields = ('id',
                  'name',
                  'city_id',
                  'address',
                  'capacity',
                  'year_of_opening')


class TeamSerializer(serializers.ModelSerializer):
    year_of_foundation = serializers.IntegerField(min_value=0, max_value=datetime.datetime.now().year)
    city_id = serializers.IntegerField()
    players = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    coach_id = serializers.PrimaryKeyRelatedField(read_only=True, many=False, source='coach')

    class Meta:
        model = Team
        fields = ('id',
                  'name',
                  'year_of_foundation',
                  'city_id',
                  'coach_id',
                  'players')


class PersonSerializer(serializers.ModelSerializer):
    country_of_birth_id = serializers.IntegerField()

    class Meta:
        model = Person
        fields = ('id',
                  'first_name',
                  'last_name',
                  'date_of_birth',
                  'country_of_birth_id')


class PlayerSerializer(serializers.ModelSerializer):
    person_id = serializers.IntegerField()
    team_id = serializers.IntegerField(required=False)
    height = serializers.IntegerField(min_value=100, max_value=250)
    weight = serializers.IntegerField(min_value=30, max_value=150)

    class Meta:
        model = Player
        fields = ('id',
                  'person_id',
                  'team_id',
                  'height',
                  'weight')

    def create(self, validated_data):
        return Player.objects.create(**validated_data)


class CoachSerializer(serializers.ModelSerializer):
    person_id = serializers.IntegerField()
    team_id = serializers.IntegerField(required=False)

    class Meta:
        model = Coach
        fields = ('id',
                  'person_id',
                  'team_id')


class MatchSerializer(serializers.ModelSerializer):
    stadium_id = serializers.IntegerField()
    home_team_id = serializers.IntegerField()
    guest_team_id = serializers.IntegerField()
    date_time = serializers.DateTimeField(format="%Y-%m-%dT%H:%M:%S")
    home_goals = serializers.IntegerField(min_value=0)
    guest_goals = serializers.IntegerField(min_value=0)
    home_total_attempts = serializers.IntegerField(min_value=0)
    guest_total_attempts = serializers.IntegerField(min_value=0)

    class Meta:
        model = Match
        fields = ('id',
                  'stadium_id',
                  'home_team_id',
                  'guest_team_id',
                  'date_time',
                  'home_goals',
                  'guest_goals',
                  'home_total_attempts',
                  'guest_total_attempts')

    def validate(self, attrs):
        instance = Match(**attrs)
        if instance.home_team_id == instance.guest_team_id:
            raise serializers.ValidationError({
                "home_team_id, guest_team_id": ["participating teams must be different."]
            })
        return attrs
