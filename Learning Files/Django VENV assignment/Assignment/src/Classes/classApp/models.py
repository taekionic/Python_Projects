from django.db import models

class djangoClasses(models.Model):
    Title = models.CharField(max_length=60)
    Course_Number = models.IntegerField()
    Instructor_Name = models.CharField(max_length=60)
    Duration = models.FloatField()
    objects = models.Manager()

    def __str__(self):
        return self.Title

