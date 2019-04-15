from django.db import models

from .nationality import Nationality


class Grantdomain(models.Model):
    """
    Represents a Grant domain in the system
    Example: public, private
    """

    grantdomain_id = models.AutoField(primary_key=True)          #: ID
    grantdomain_domain = models.CharField('Domain', max_length=200)  #: Name

    class Meta:
        verbose_name = "Domain"
        verbose_name_plural = "Domains"
        app_label = 'finance'

    def __str__(self):
        return self.grantdomain_domain


class Grantor(models.Model):
    """
    Represents a Grant grantor in the system
    Example: Bial, FCT
    """

    grantor_id = models.AutoField(primary_key=True)          #: ID
    grantor_name = models.CharField('Name', max_length=200)  #: Name
    grantor_icon = models.ImageField('Icon',
        blank=True, null=True,
        upload_to='finance/grantor/grantor_icon', max_length=255)

    class Meta:
        verbose_name = "Grantor"
        verbose_name_plural = "Grantors"
        ordering = ['grantor_name',]
        app_label = 'finance'

    def __str__(self):
        return self.grantor_name


class Grant(models.Model):
    """
    Represents a Grant in the system
    Example: PZLOC
    """

    grant_id = models.AutoField(primary_key=True)          #: ID
    grant_name = models.CharField('Name', max_length=200)  #: Name
    #grant_responsible = models.CharField('Responsible', max_length=200)  #: Responsible Name
    #grant_lab = models.CharField('Lab', max_length=200)  #: Lab Name


    nationality = models.ForeignKey(Nationality, verbose_name='Grant nationality', on_delete=models.CASCADE)  #: Grant Nationality
    domain = models.ForeignKey(Grantdomain, verbose_name='Grant domain', on_delete=models.CASCADE)  #: Grant Domain
    grantor = models.ForeignKey(Grantor, verbose_name='Grantor', on_delete=models.CASCADE)  #: Grantor

    class Meta:
        verbose_name = "Grant"
        verbose_name_plural = "Grants"
        app_label = 'finance'

    def __str__(self):
        return self.grant_name
