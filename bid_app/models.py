from django.db import models
from market_place.models import Product
# Create your models here.
class Bid(models.Model):
    product_id = models.CharField(blank=False, max_length=50)
    bid_amt = models.CharField(blank=False,max_length=20)
    bid_by = models.CharField(blank=False,max_length=50)
    status = models.CharField(max_length=1,blank=False)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        product_name = Product.objects.get(id=self.product_id)
        return product_name.company_name +' '+ product_name.model +' '+ product_name.sub_class
