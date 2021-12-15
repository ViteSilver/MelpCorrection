# Generated by Django 3.2.10 on 2021-12-10 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurants',
            fields=[
                ('id', models.TextField(primary_key=True, serialize=False)),
                ('rating', models.IntegerField()),
                ('name', models.TextField()),
                ('site', models.TextField()),
                ('email', models.TextField()),
                ('phone', models.TextField()),
                ('street', models.TextField()),
                ('city', models.TextField()),
                ('state', models.TextField()),
                ('lat', models.FloatField()),
                ('lng', models.FloatField()),
            ],
        ),
    ]
