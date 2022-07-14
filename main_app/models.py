from django.urls import reverse
from django.db import models
from django.core.validators import MaxValueValidator
from django.core.validators import MinValueValidator

# Create your models here.

class Tag(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('tags_detail', kwargs={'tag_id': self.id})

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
    tags = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'travel_id': self.id})

class Reviews(models.Model):
    review = models.TextField(max_length=300)
    name = models.CharField(max_length=100)
    
    travel = models.ForeignKey(Travel, on_delete=models.CASCADE)

    def __str__(self):
        return self.review