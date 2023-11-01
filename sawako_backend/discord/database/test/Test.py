from django.db import models


class Test(models.Model):
    name = models.CharField(max_length=20)
    image = models.ImageField(upload_to='tests/')

    class Meta:
        app_label = 'discord'