from django.db import models

from core.models import CreateTimeStampedModel, GetUniqueOrNoneManager


class Picture(CreateTimeStampedModel):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=1024, null=True, blank=True)
    height = models.PositiveIntegerField()
    width = models.PositiveIntegerField()
    image = models.ImageField(upload_to="users/images/", height_field='height', width_field='width')
    objects = GetUniqueOrNoneManager()

    def __unicode__(self):
        return self.title

    class Meta:
        db_table = 'picture'