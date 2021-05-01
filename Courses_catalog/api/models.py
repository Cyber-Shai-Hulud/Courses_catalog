from django.db import models


# Creating our courses model
class Courses(models.Model):
    name = models.CharField(max_length=120)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)
    amount = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name
