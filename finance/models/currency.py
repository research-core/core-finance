from django.db import models


class Currency(models.Model):
    """
    Represents a Currency of an order in the system
    """

    currency_id = models.AutoField(primary_key=True)  #: Pk ID
    currency_name = models.CharField('Name', max_length=100) #: Name
    currency_symbol = models.CharField('Symbol', max_length=100, unique=True)

    class Meta:
        verbose_name = "Currency"
        verbose_name_plural = "Currencies"
        app_label = 'finance'

    def __str__(self):
        return self.currency_symbol

    @staticmethod
    def autocomplete_search_fields():
        return (
            'currency_name__icontains',
        )
