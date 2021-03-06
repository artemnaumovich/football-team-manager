# Generated by Django 3.0.5 on 2020-04-17 15:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_remove_team_home_stadium'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('date_of_birth', models.DateField()),
                ('country_of_birth', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='people', to='api.Country')),
            ],
        ),
    ]
