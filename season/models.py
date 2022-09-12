from django.db import models


class Season(models.Model):
    choices = (('Fall', 'Fall'), ('Winter', 'Winter'), ('Summer', 'Summer'), ('Spring', 'Spring'))
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    season = models.CharField(max_length=255, null=True)

    def __str__(self):
        datestr= str(self.date)
        return datestr
