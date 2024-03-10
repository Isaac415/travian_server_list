from django.db import models

# Create your models here.
class GameWorld(models.Model):
    id = models.CharField(max_length=200, primary_key=True)
    url = models.URLField()
    server = models.CharField(max_length=200)
    speed = models.CharField(max_length=200)
    game_mode = models.CharField(max_length=200)
    num_of_tribes = models.IntegerField()
    start_date = models.CharField(max_length=200)
    start_time = models.CharField(max_length=200)
    artifacts_spawn_date = models.CharField(max_length=200)
    building_plans_spawn_date = models.CharField(max_length=200)
    end_condition = models.CharField(max_length=200)