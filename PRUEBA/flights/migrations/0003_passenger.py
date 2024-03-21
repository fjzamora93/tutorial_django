# Generated by Django 5.0.3 on 2024-03-21 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0002_airport_remove_flight_destinatio_flight_destination_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.CharField(max_length=64)),
                ('last', models.CharField(max_length=64)),
                ('flights', models.ManyToManyField(blank=True, related_name='passengers', to='flights.flight')),
            ],
        ),
    ]