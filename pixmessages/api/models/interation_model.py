from django.db import models


class Interaction(models.Model):
    id = models.CharField(max_length=12, primary_key=True)
    ispb = models.CharField(max_length=8)
    date_created = models.DateTimeField(auto_now_add=True, editable=False)
    date_used = models.DateTimeField(null=True)
