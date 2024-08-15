# from django.db import models
#
#
# class MasterChef(models.Model):
#     name = models.CharField(max_length=100)
#     bio = models.TextField()
#     photo = models.ImageField(upload_to='chefs_photos')
#     specializations = models.CharField(max_length=255)
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name_plural = 'Master Chefs'
#         # ordering = ('sort',)


# from django.db import models
#
#
# class MasterChef(models.Model):
#     name = models.CharField(max_length=50)
#     position = models.CharField(max_length=50)
#     photo = models.ImageField(upload_to='masters_photos')
#     is_visible = models.BooleanField(default=True)
#     sort = models.PositiveSmallIntegerField()
#
#     facebook = models.URLField(blank=True)
#     twitter = models.URLField(blank=True)
#     linkedin = models.URLField(blank=True)
#
#     class Meta:
#         verbose_name_plural = 'MasterChefs'
#         ordering = ('sort', )
#
#     def __str__(self):
#         return self.name



from django.db import models


# Create your models here.
class Staff(models.Model):
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='staff_photos')
    is_visible = models.BooleanField(default=True)
    sort = models.PositiveSmallIntegerField()

    facebook = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)

    class Meta:
        verbose_name_plural = 'Staff'
        ordering = ('sort', )

    def __str__(self):
        return self.name
