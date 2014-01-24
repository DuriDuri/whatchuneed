from django.db import models

# Create your models here.
# Create your models here.
class Offer(models.Model):
    name = models.CharField(max_length = 250)
    email = models.EmailField(max_length=18)
    phone = models.CharField(max_length=250)
    deliver_what = models.CharField(max_length = 250)
    deliver_where = models.CharField(max_length = 250)
    offer_for_delivery = models.CharField(max_length = 250)
    length_of_offer = models.CharField(max_length = 250, null=True, blank=True)
    offer_placed = models.DateTimeField(auto_now_add =True, auto_now=False)
    
    def __unicode__(self):
        return self.email
    
    class Meta:
        ordering = ['-offer_placed',]
    
