from django.db import models


class User(models.Model):
    id = models.BigIntegerField(primary_key=True)
