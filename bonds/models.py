from django.db import models

# Create your models here.
class Bond(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    issuer = models.CharField(max_length=10)
    term = models.IntegerField()
    parValue = models.FloatField()
    couponRate = models.FloatField()
    owner = models.ForeignKey('auth.User',
                              related_name='bonds',
                              on_delete=models.CASCADE)

    class Meta:
        ordering = ('created',)

class Company(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    ticker = models.CharField(max_length=5)
    revenue = models.FloatField()
    netIncome = models.FloatField()
    noOfEmployees = models.IntegerField()
    owner = models.ForeignKey('auth.User',
                              related_name='companies',
                              on_delete=models.CASCADE)

    class Meta:
        ordering = ('created',)
    
