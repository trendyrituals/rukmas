from django.db import models

# Create your models here.
class Detail(models.Model):
    about = models.TextField(blank=False)

    def __str__(self):
        return "Page Details"



class Team_member(models.Model):
    name = models.CharField(blank=False, max_length=100)
    mobile = models.CharField(blank=False,max_length=10)
    email = models.CharField(blank=False,max_length=100)
    img = models.ImageField(blank=False)
    view = models.TextField(blank=False)

    def __str__(self):
        return self.name


class Working_process(models.Model):
    heading = models.CharField(blank=False,max_length=100)
    img = models.ImageField(blank=False)
    detail = models.TextField(blank=False)

    def __str__(self):
        return self.heading
