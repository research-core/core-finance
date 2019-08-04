from django.db import models
from .costcenter_queryset import CostCenterQuerySet


class CostCenter(models.Model):
    """
    Represents a Finance cost center in the system
    Example: CCU
    """
    costcenter_id   = models.AutoField(primary_key=True)          #: ID
    costcenter_name = models.CharField('Name', max_length=200)  #: Name
    costcenter_code = models.CharField('Code', max_length=200)  #: Code

    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    group = models.ForeignKey('auth.Group', verbose_name='Group', blank=False, null=False, on_delete=models.CASCADE) #: Research group use this project. is a Fk to the Group table

    objects = CostCenterQuerySet.as_manager()

    class Meta:
        ordering            = ['costcenter_code',]
        verbose_name        = "Finance Cost Center"
        verbose_name_plural = "Finance Cost Centers"
        app_label           = 'finance'

    def __str__(self):
        return "{0} - {1}".format(self.costcenter_code, self.costcenter_name)
