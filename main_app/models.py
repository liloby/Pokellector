from django.db import models
from django.urls import reverse

INTERACTS = (
    ('P', 'Pet'),
    ('G', 'Groom'),
    ('F', 'Feed'),

)

# Create your models here.
class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    level = models.IntegerField()
    description = models.TextField(max_length=250)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pokemon_id': self.id})

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