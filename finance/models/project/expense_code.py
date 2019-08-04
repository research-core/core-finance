from django.db import models
from finance.models.project.project import Project


class ExpenseCode(models.Model):
    """
    Represents a Budget of an order in the system
    """

    expensecode_id = models.AutoField(primary_key=True)  #: Pk ID
    expensecode_number = models.CharField('ExpenseCode Number', max_length=100) #: Name
    expensecode_type = models.CharField('ExpenseCode Type', max_length=100) #: Type

    financeproject = models.ForeignKey(Project, verbose_name='Finance Project', on_delete=models.CASCADE)

    @staticmethod
    def autocomplete_search_fields():
        return ("expensecode_number",
            'expensecode_type__icontains',
            'financeproject__financeproject_name__icontains',
            'financeproject__financeproject_code',
            'financeproject__costcenter__costcenter_code',
            'financeproject__costcenter__costcenter_name__icontains' )


    class Meta:
        verbose_name = "Expense Code"
        verbose_name_plural = "Expense Codes"
        unique_together = ("expensecode_number", "financeproject")
        app_label = 'finance'

    """
    def __str__(self):
        return self.expensecode_number
    """

    def __str__(self):
        return self.financeproject.costcenter.costcenter_code + "-" + \
        self.financeproject.financeproject_code+"-"+ \
        self.expensecode_number+": "+self.financeproject.costcenter.costcenter_name+"-"+ \
        self.financeproject.financeproject_name+"-"+self.expensecode_type

    def expensecode(self):
        return str(self.financeproject.costcenter.costcenter_code + "-" + \
        self.financeproject.financeproject_code+"-"+ \
        self.expensecode_number+": "+self.financeproject.costcenter.costcenter_name+"-"+ \
        self.financeproject.financeproject_name+"-"+self.expensecode_type )

    @property
    def abbrv(self):
        """Returns a string with codes only, i.e. `CCCCCCC-PPP-EE`."""
        cost_center = self.financeproject.costcenter.costcenter_code
        project = self.financeproject.financeproject_code
        expense_code = self.expensecode_number
        return f'{cost_center}-{project}-{expense_code}'
