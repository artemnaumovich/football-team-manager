from django.test import TestCase, Client
from rest_framework import status
from .models import(
    Country,
    City,
    Person,
    Coach,
    Team
)
import json

import json


# Create your tests here.

client = Client()


class CountryTestCase(TestCase):
    def setUp(self):
        Country.objects.create(name='Ukraine')

    def test_find_not_Ukraine(self):
        nothing = list(Country.objects.exclude(name='Ukraine'))
        self.assertEqual(nothing, [])


class ShakhtarTestCase(TestCase):
    def setUp(self):
        Ukraine = Country.objects.create(name='Ukraine')
        Donetsk = City.objects.create(name='Donetsk', country=Ukraine)
        Shakhtar = Team.objects.create(name='Shakhtar', city=Donetsk,
                                       year_of_foundation=1936)
        Portugal = Country.objects.create(name='Portugal')
        LuisCastro = Person.objects.create(first_name='Luis', last_name='Castro',
                                       date_of_birth='1961-09-03',
                                       country_of_birth=Portugal)
        Coach.objects.create(person=LuisCastro, team=Shakhtar)


    def test_check_Donetsk_country(self):
        Donetsk = City.objects.get(name='Donetsk')
        Ukraine_name = Donetsk.country.name
        self.assertEqual(Ukraine_name, 'Ukraine')


    def test_check_Shakhtar_coach(self):
        Shakhtar = Team.objects.get(name='Shakhtar')
        LuisCastro = Shakhtar.coach.person
        self.assertEqual(Shakhtar.name, 'Shakhtar')
        self.assertEqual(LuisCastro.first_name, 'Luis')
        self.assertEqual(LuisCastro.last_name, 'Castro')


class PostRequestTestCase(TestCase):
    def setUp(self):
        England = Country.objects.create(name='England')
        London = City.objects.create(name='London', country=England)
        self.valid_payload = {
            'name': 'Arsenal',
            'city_id': London.id,
            'year_of_foundation': 1800
        }
        self.invalid_payload = {
            'name': 'Arsenal',
            'city_id': London.id,
            'year_of_foundation': -1024
        }


    def test_create_valid_team(self):
        response = client.post(
            '/api/team/',
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


    def test_create_invalid_team(self):
        response = client.post(
            '/api/team/',
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
