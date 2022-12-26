from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.


class Player(models.Model):
    POS = [
        ('PG', 'Point Guard'),
        ('SG', 'Shooting Guard'),
        ('SF', 'Small Forward'),
        ('PF', 'Power Forward'),
        ('C', 'Center')
    ]

    full_name = models.CharField(max_length=50)
    number = models.CharField(max_length=2)
    position = models.CharField(max_length=2, choices=POS)
    height = models.CharField(max_length=5)
    weight = models.IntegerField()
    birth_date = models.CharField(max_length=50)
    experience = models.IntegerField()
    college = models.CharField(max_length=40)
    slug = models.SlugField(null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.full_name)
        
        super(Player, self).save(*args, **kwargs)


    def __str__(self):
        return self.full_name

