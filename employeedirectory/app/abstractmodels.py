import uuid
from django.db import models


def make_uuid():
    """ Return UUID string """
    return str(uuid.uuid4())


class MyModel(models.Model):

    id = models.UUIDField(primary_key=True, max_length=36, unique=True,
                          db_index=True, default=self.__make_uuid(), editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
