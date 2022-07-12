from django.db import models
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator

# Create your models here.

class Travel(models.Model):
    title = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    rating = models.PositiveIntegerField(
        default=0,
        validators=[
            MaxValueValidator(10),
            MinValueValidator(0)
        ]
    )

    def __str__(self):
        return self.title