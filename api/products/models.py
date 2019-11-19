from django.db import models
from pygments.formatters.html import HtmlFormatter

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    img = models.CharField(max_length=100, blank=True, default='')
    price = models.IntegerField(blank=True, null=True)
    company = models.CharField(max_length=100, default='', blank=True)
    info = models.CharField(max_length=1000, default='', blank=True)
    inCart = models.BooleanField(default=False)
    count = models.IntegerField(blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id']