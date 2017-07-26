from django.db import models

# Create your models here.
class Resume(models.Model):
    name = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='photo', blank=True)
    address = models.CharField(max_length=200)
    father = models.CharField(max_length=255)
    mother = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    cgpa = models.FloatField()
    university = models.CharField(max_length=255)
    certificate = models.CharField(max_length=255, blank=True)
    skills = models.TextField()

    def __str__(self):
        return self.name
