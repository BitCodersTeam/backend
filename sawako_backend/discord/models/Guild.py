from django.db import models


class Guild(models.Model):
    id = models.BigIntegerField(primary_key=True)
    setting = models.TextField()