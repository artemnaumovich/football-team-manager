# Generated by Django 3.0.5 on 2020-04-20 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0019_auto_20200419_1522'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coach',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('person', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='coach', to='api.Person')),
                ('team', models.OneToOneField(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='coach', to='api.Team')),
            ],
        ),
    ]
