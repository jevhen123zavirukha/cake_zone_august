from django.db import models


class MasterChef(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    photo = models.ImageField(upload_to='chefs_photos')
    specializations = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Master Chefs'
        # ordering = ('sort',)
