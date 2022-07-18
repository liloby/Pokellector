from django.db import models
from django.urls import reverse
from datetime import date

INTERACTS = (
    ('P', 'Pet'),
    ('G', 'Groom'),
    ('F', 'Feed'),

)

class Move(models.Model):
    name = models.CharField(max_length=50)
    level_requirement = models.IntegerField()
    type = models.CharField(max_length=20)
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('moves_detail', kwargs={'pk': self.id})

    class Meta:
        ordering = ['name']

# Create your models here.
class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    level = models.IntegerField()
    description = models.TextField(max_length=250)

    moves = models.ManyToManyField(Move)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pokemon_id': self.id})
    
    def interact_for_today(self):
        return self.interaction_set.filter(date=date.today()).count() 

class Interaction(models.Model):
    date = models.DateField()
    interact = models.CharField(
        max_length=1,
        choices=INTERACTS,
        default=INTERACTS[0][0]
        )

    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.get_interact_display()} on {self.date}"

    class Meta:
        ordering = ['-date']