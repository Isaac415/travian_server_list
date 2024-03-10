# Generated by Django 4.2.3 on 2024-03-10 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GameWorld',
            fields=[
                ('id', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('url', models.URLField()),
                ('server', models.CharField(max_length=200)),
                ('speed', models.CharField(max_length=200)),
                ('game_mode', models.CharField(max_length=200)),
                ('num_of_tribes', models.IntegerField()),
                ('start_date', models.CharField(max_length=200)),
                ('start_time', models.CharField(max_length=200)),
                ('artifact_spawn_date', models.CharField(max_length=200)),
                ('building_plans_spawn_date', models.CharField(max_length=200)),
                ('end_condition', models.CharField(max_length=200)),
            ],
        ),
    ]
