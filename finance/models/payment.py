from django.db import models


class PaymentFrequency(models.Model):
    """
    Represents a Person's salry Currency in the system
    Example: Euro, Dolar
    """

    paymentfrequency_id = models.AutoField(primary_key=True)        #: ID
    paymentfrequency_name = models.CharField('Name', max_length=70) #: Name

    class Meta:
        ordering = ['paymentfrequency_name',]
        verbose_name = "Payment frequency"
        verbose_name_plural = "Payments frequencies"
        app_label = 'common'

    def __str__(self):
        return self.paymentfrequency_name
