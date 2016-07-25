from django.db import models

class SyllableSample(models.Model):
    # This is the path below STATIC_ROOT or STATIC_URL where the sample can be found.
    path = models.FilePathField()
    sound = models.CharField(max_length=10)
    tone = models.IntegerField()
    display = models.CharField(max_length=10)
