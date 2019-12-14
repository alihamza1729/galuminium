

from django.db import models



# Create your models here.



class Store(models.Model):
    section = models.CharField(max_length=10)
    color = models.CharField(max_length=20)
    size = models.FloatField()
    quantity = models.FloatField()
    thickness = models.FloatField()
    rate = models.FloatField()


    def __str__(self):
        return self.section

    def get_absolute_url(self):
        return "/store/%s/" % self.id

    class Meta:
        ordering = ["-id"]
