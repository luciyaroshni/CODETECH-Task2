from django.db import models

# Create your models here.


class Fileupload(models.Model):
    fileuploadno = models. AutoField(primary_key=True)
    fileuploadname = models.CharField(max_length=25)
    fileupload = models.FileField(upload_to='uploads/')