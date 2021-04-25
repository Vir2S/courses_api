from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=1000)
    start_date = models.DateField()
    end_date = models.DateField()
    lectures = models.IntegerField()

    def __str__(self):
        return self.title
