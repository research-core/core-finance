from django.db import models
from django.contrib.auth.models import Group

class OrderACL(models.Model):
    acltable_id = models.AutoField('Id', primary_key=True)

    foreign = models.ForeignKey("Order", on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)


    class Meta:
        app_label = 'finance'