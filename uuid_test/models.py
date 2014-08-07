import uuid

from django.db import models


class PrimaryKey(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class SecondaryKey(models.Model):
    uid = models.UUIDField(editable=False, default=uuid.uuid4)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class NotAKey(models.Model):
    uid = models.UUIDField(default=uuid.uuid4)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
