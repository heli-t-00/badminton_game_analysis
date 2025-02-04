from django.db import models

# Create your models here.
#User Model
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    profile_picture = models.ImageField(upload_to='Users/', blank=True, null=True)

    def fullname(self):
        return self.first_name + " " + self.last_name
    def __str__(self):
        return f"{self.fullname(), self.email}"

#Game Model
class Game(models.Model):
    game_name = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    date_played = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.game_name

#Point Model
class Point(models.Model):
    point=models.IntegerField(default=0)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    game=models.ForeignKey(Game, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

#Shot Model
class Shot(models.Model):
    shot_name=models.CharField(max_length=100)
    position = models.FloatField()
