from django.db import models


class Nationality(models.Model):
    """
    Represents a Grant nationality in the system
    Example: USA, Portugal
    """

    nationality_id = models.AutoField(primary_key=True)          #: ID
    nationality_name = models.CharField('Nationality', max_length=200)  #: Name

    class Meta:
        verbose_name = "Nationality"
        verbose_name_plural = "Nationalities"
        app_label = 'finance'

    def __str__(self):
        return self.nationality_name
