from django.db import models

# Create your models here.
class PersonalInfo(models.Model):
    GENDER_CHOICE = (
		("Male", "Male"),
		("Female", "Female"),
	)

    name = models.CharField(max_length=150)
    photo = models.ImageField(upload_to='photo', blank=True)
    address = models.CharField(max_length=200)
    father = models.CharField(max_length=255)
    mother = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    cgpa = models.FloatField()
    birth_day = models.DateField()
    gender = models.CharField(max_length=6, choices=GENDER_CHOICE)
    nationality = models.CharField(max_length=25)
    phone_no = models.CharField(max_length=14, blank=True)

    def __str__(self):
        return self.name

class WorkExperience(models.Model):
	company_name = models.CharField(max_length=50)
	job_title = models.CharField(max_length=20)
	joining_year = models.DateField(null=True, blank=True)
	job_description = models.TextField()

class Education(models.Model):
	institute_name = models.CharField(max_length=50, blank=False)
	subject = models.CharField(max_length=40)
	year = models.DateField(null=True, blank=True)
	description = models.TextField()

class Skills(models.Model):
	language_skills = models.CharField(max_length=200, blank=True, help_text="Sparate languages by comma")
	other_skills = models.CharField(max_length=200, blank=True, help_text="Sparate Skills by comma")
