# Generated by Django 3.0.5 on 2020-04-17 19:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_auto_20200417_2213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='person',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='player', to='api.Person'),
        ),
    ]
