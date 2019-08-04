from django.db import models

try:
    from django.urls import reverse
except ImportError:
    from django.core.urlresolvers import reverse


class Budget(models.Model):
    """
    Represents a Budgets in the system
    """

    budget_id = models.AutoField(primary_key=True)  #: ID
    budget_amount = models.DecimalField('Amount (NET)', max_digits=11, decimal_places=2)    #: Amount for that budget                           #: First Name
    budget_year = models.IntegerField('Year', blank=True, null=True)  #: Budget year

    expensecode = models.ForeignKey('ExpenseCode', verbose_name='Expense Code', on_delete=models.CASCADE) #: projects that are related to this budget
    #group = models.ForeignKey(Group, verbose_name='Group', on_delete=models.CASCADE) #: the group in the cnp that has this budget

    class Meta:
        verbose_name = "Budget"
        verbose_name_plural = "Budgets"
        unique_together = (('budget_year','expensecode'),)
        #ordering = ['expensecode__financeproject__costcenter__costcenter_code', 'expensecode__financeproject__financeproject_code']
        app_label = 'finance'

    def amount(self):
        return "{:,.2f}".format(self.budget_amount).replace(".","#").replace(",",".").replace("#",",")

    def __str__(self):
        #return str(self.budget_amount)
        return self.amount()#return "$ %s" % intcomma(str(self.budget_amount))
