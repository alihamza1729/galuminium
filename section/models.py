from django.db import models


# Create your models here.
class Section(models.Model):
    section_name = models.CharField(max_length=10)
    section_color = models.CharField(max_length=20)
    section_size = models.FloatField()
    section_thickness = models.FloatField()
    section_rate = models.FloatField()

    def __str__(self):
        return self.section_name

    def get_absolute_url(self):
        return "/section/%s/" % self.id

    class Meta:
        db_table = 'section'
