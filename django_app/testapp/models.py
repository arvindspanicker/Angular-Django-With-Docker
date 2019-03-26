from django.db import models


class TestModel(models.Model):
    title = models.CharField(default='',blank=True,null=False,max_length=20)
    updated_at = models.DateTimeField(blank=True,null=True)