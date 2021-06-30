from django.db import models

# Create your models here.
class Product(models.Model):
    username = models.CharField(max_length=50)
    company_name = models.CharField(blank=False, max_length=50)
    model = models.CharField(blank=False, max_length=50)
    sub_class = models.CharField(blank=False, max_length=50)
    year = models.CharField(blank=False, max_length=10)
    fuel_type = models.CharField(blank=False, max_length=50)
    body_type = models.CharField(blank=False, max_length=50)
    color = models.CharField(blank=False, max_length=50)
    transmission_type = models.CharField(blank=False, max_length=50)
    location = models.CharField(blank=False, max_length=50)
    registration_state = models.CharField(blank=False, max_length=50)
    driven = models.CharField(blank=False, max_length=50)
    number_of_owner = models.CharField(blank=False, max_length=50)
    condition_grade = models.CharField(blank=False, max_length=50)
    expected_price = models.CharField(blank=False, max_length=50)
    img = models.ImageField(blank=False)
    status = models.CharField(blank=False, max_length=1)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.company_name+' '+self.model+' '+self.sub_class
