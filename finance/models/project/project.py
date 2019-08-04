from django.db import models
from .project_queryset import ProjectQuerySet

class Project(models.Model):
    """
    Represents Project in the system
    """

    financeproject_id   = models.AutoField(primary_key=True)       #: Pk ID
    financeproject_name = models.CharField('Name', max_length=200) #: Name
    financeproject_code = models.CharField('Code', max_length=200, unique=True) #: Number

    # Grant section
    financeproject_startdate   = models.DateField('Starting date', blank=True, null=True) #: Starting date of the grant
    financeproject_enddate     = models.DateField('Ending date', blank=True, null=True) #: Ending date of the grant
    financeproject_totalamount = models.DecimalField('Total amount', blank=True, null=True,max_digits=11, decimal_places=2)  #: Total amount of the grant
    financeproject_overheads   = models.DecimalField('Overhead', blank=True, null=True,max_digits=11, decimal_places=2)  #: Overhead amount of the grant
    financeproject_funding     = models.DecimalField('Funding', blank=True, null=True,max_digits=11, decimal_places=2)  #: Funding amount of the grant
    financeproject_responsible = models.CharField('Responsible', max_length=200)  #: Responsible Name

    costcenter = models.ForeignKey('CostCenter', verbose_name='Cost Center', on_delete=models.CASCADE)   #: Finance Cost Center is a Fk to that table
    currency   = models.ForeignKey('common.Currency', verbose_name='Currency', blank=True, null=True, on_delete=models.CASCADE) #: Currency of the grant
    grant      = models.ForeignKey('Grant', verbose_name='Grant', blank=True, null=True, on_delete=models.CASCADE) #: Currency of the grant

    objects = ProjectQuerySet.as_manager()

    class Meta:
        ordering = ['financeproject_code', 'costcenter']
        verbose_name = "Finance Project"
        verbose_name_plural = "Finance Projects"
        app_label = 'finance'

    def __str__(self):
        costcenter = self.costcenter
        if costcenter!=None:
            return costcenter.costcenter_code + "-" + self.financeproject_code+ ": " + costcenter.costcenter_name + "-" + self.financeproject_name
        else:
            return "No FinanceCostCenter associated - " + self.financeproject_name + " - " + self.financeproject_code

    # Custom methods

    def nationality(self):
        if self.grant is None:
            return ""
        return str(self.grant.nationality)

    def domain(self):
        if self.grant is None:
            return ""
        return str(self.grant.domain)

    def grantor(self):
        if self.grant is None:
            return ""
        return str(self.grant.grantor)

    # Methods used by PyForms

    # @staticmethod
    # def get_queryset(request, qs):
    #     user = request.user

    #     if user.is_superuser: return qs
    #     if user.groups.filter(name=settings.PROFILE_HUMAN_RESOURCES).exists(): return qs
    #     qs = qs.filter(group__members__djangouser=user)
    #     return qs

    @staticmethod
    def autocomplete_search_fields():
        return (
            'financeproject_name__icontains',
            'financeproject_code__icontains',
            'costcenter__costcenter_name__icontains',
            'costcenter__costcenter_code__icontains'
        )
