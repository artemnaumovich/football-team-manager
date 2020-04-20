from rest_framework import serializers

from .models import (
    Country,
    City,
    Stadium,
    Team,
    Person,
    Player,
    Coach
)


class CitySerializer(serializers.ModelSerializer):
    country_id = serializers.IntegerField()
    stadiums = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    teams = serializers.PrimaryKeyRelatedField(read_only=True, many=True)

    class Meta:
        model = City
        fields = ('id', 'name', 'country_id', 'stadiums', 'teams')


class CountrySerializer(serializers.ModelSerializer):
    cities = serializers.PrimaryKeyRelatedField(read_only=True, many=True)

    class Meta:
        model = Country
        fields = ('id', 'name', 'cities')


class StadiumSerializer(serializers.ModelSerializer):
    city_id = serializers.IntegerField()
    capacity = serializers.IntegerField(min_value=0)
    year_of_opening = serializers.IntegerField(min_value=0)

    class Meta:
        model = Stadium
        fields = ('id', 'name', 'city_id', 'address', 'capacity', 'year_of_opening')


class TeamSerializer(serializers.ModelSerializer):
    year_of_foundation = serializers.IntegerField(min_value=0)
    city_id = serializers.IntegerField()
    players = serializers.PrimaryKeyRelatedField(read_only=True, many=True)
    coach_id = serializers.PrimaryKeyRelatedField(read_only=True, many=False, source='coach')

    class Meta:
        model = Team
        fields = ('id', 'name', 'year_of_foundation', 'city_id', 'coach_id', 'players')


class PersonSerializer(serializers.ModelSerializer):
    country_of_birth_id = serializers.IntegerField()

    class Meta:
        model = Person
        fields = ('id', 'first_name', 'last_name', 'date_of_birth', 'country_of_birth_id')


class PlayerSerializer(serializers.ModelSerializer):
    person_id = serializers.IntegerField()
    team_id = serializers.IntegerField(required=False)

    class Meta:
        model = Player
        fields = ('id', 'person_id', 'team_id')

    def create(self, validated_data):
        return Player.objects.create(**validated_data)


class CoachSerializer(serializers.ModelSerializer):
    person_id = serializers.IntegerField()
    team_id = serializers.IntegerField(required=False)

    class Meta:
        model = Coach
        fields = ('id', 'person_id', 'team_id')