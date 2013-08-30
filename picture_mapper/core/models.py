from django.db import models
from django.contrib.auth.models import User
"""
Models for core app.
"""


class CreateTimeStampedModel(models.Model):
    """
    An abstract base class model that provides selfupdating ``created`` and ``modified`` fields,
    and an author field that records the user that created the model instance
    """

    author = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class GetUniqueOrNoneManager(models.Manager):
    """Adds get_unique_or_none method to objects"""

    def get_unique_or_none(self, **kwargs):
        try:
            return self.get(**kwargs)
        except (self.model.DoesNotExist, self.model.MultipleObjectsReturned):
            return None
