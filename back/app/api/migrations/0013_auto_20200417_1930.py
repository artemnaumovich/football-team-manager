# Generated by Django 3.0.5 on 2020-04-17 16:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_player'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='id',
        ),
        migrations.AlterField(
            model_name='player',
            name='person',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='player', serialize=False, to='api.Person'),
        ),
    ]
