from django.db import models
from home.models import Establishment


class ContactInfo(models.Model):
    establishment = models.OneToOneField(Establishment, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()
    working_hours = models.CharField(max_length=100)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return self.establishment.name

    class Meta:
        verbose_name_plural = 'Contact information'
