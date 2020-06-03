from django.db import models

# Create your models here.


class Country(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=100, unique=True)
    country = models.ForeignKey(Country, related_name='cities', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Stadium(models.Model):
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City, related_name='stadiums', on_delete=models.CASCADE)
    address = models.CharField(max_length=100)
    capacity = models.PositiveIntegerField()
    year_of_opening = models.IntegerField()

    class Meta:
        unique_together = [['city', 'address'], ]

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=100)
    year_of_foundation = models.IntegerField()
    city = models.ForeignKey(City, related_name='teams', on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    country_of_birth = models.ForeignKey(Country, related_name='people', on_delete=models.CASCADE)

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class Player(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE, related_name='player')
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, related_name='players', blank=True, default=None, null=True)
    height = models.PositiveIntegerField()
    weight = models.PositiveIntegerField()

    def __str__(self):
        return '{}({})'.format(self.person, self.team)


class Coach(models.Model):
    person = models.OneToOneField(Person, on_delete=models.CASCADE, related_name='coach')
    team = models.OneToOneField(Team, on_delete=models.SET_NULL, related_name='coach', blank=True, default=None, null=True)

    def __str__(self):
        return '{}({})'.format(self.person, self.team)


class Match(models.Model):
    stadium = models.ForeignKey(Stadium, on_delete=models.CASCADE, related_name='matches')
    home_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='home_matches')
    guest_team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name='guest_matches')
    date_time = models.DateTimeField()
    home_goals = models.PositiveIntegerField()
    guest_goals = models.PositiveIntegerField()
    home_total_attempts = models.PositiveIntegerField()
    guest_total_attempts = models.PositiveIntegerField()