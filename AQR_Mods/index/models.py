from django.db import models

# Create your models here.

class Mod(models.Model):
    id = models.IntegerField(primary_key=True, verbose_name="mod_id")
    Name = models.CharField(max_length=128)
    Version = models.CharField(max_length=128)
    Description = models.CharField(max_length=25565)
    DownloadURL = models.CharField(max_length=1024)

    def __str__(self):
        return f'{self.id}:{self.Name.replace(' ','_').replace('-','_')} - {self.Version}'