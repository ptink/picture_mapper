from decimal import Decimal
from django.db import models
from django.core.exceptions import ValidationError
from core.models import CreateTimeStampedModel, GetUniqueOrNoneManager


def latitude_validator(value):
    if not Decimal('-90') <= value <= Decimal('90'):
        raise ValidationError(u'%s not a valid latitude.' % value)


def longitude_validator(value):
    if not Decimal('-180') <= value <= Decimal('180'):
        raise ValidationError(u'%s not a valid longitude.' % value)


class Picture(CreateTimeStampedModel):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=1024, null=True, blank=True)
    height = models.PositiveIntegerField()
    width = models.PositiveIntegerField()
    image = models.ImageField(upload_to="users/images/", height_field='height', width_field='width')
    latitude = models.DecimalField(max_digits=10, decimal_places=8, validators=[latitude_validator])
    longitude = models.DecimalField(max_digits=11, decimal_places=8, validators=[longitude_validator])

    objects = GetUniqueOrNoneManager()

    def __unicode__(self):
        return self.title

    class Meta:
        db_table = 'picture'