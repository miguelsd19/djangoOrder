from django.db import models

class Weather(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    rain = models.BooleanField()

    def __str__(self):
        datestr= str(self.date)
        return datestr
