from django.db import models


# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=11)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return "/customer/%s/" % self.id

    class Meta:
        db_table = 'customer'
