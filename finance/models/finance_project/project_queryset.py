from django.db import models
from django.utils import timezone
from django.db.models import Q

class ProjectQuerySet(models.QuerySet):

    def active(self):
        now = timezone.now()
        return self.filter(
            (Q(financeproject_startdate=None) & Q(financeproject_enddate=None)) |
            (Q(financeproject_startdate__lte=now) and Q(financeproject_enddate=None)) |
            (Q(financeproject_startdate=None) and Q(financeproject_enddate__gte=now)) |
            (Q(financeproject_startdate__lte=now) and Q(financeproject_enddate__gte=now))
        )