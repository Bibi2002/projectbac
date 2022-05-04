from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
class Tagam(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField(blank=True)

    def get_absolute_url(self):
        return f'/esep/{self.id}'

class Makal(models.Model):
    content = models.TextField(blank=True)
    title = models.CharField(max_length=250)

class Pikir(models.Model):
    title = models.TextField(blank=True)

    def get_number(self):
        return 7

    def get_true(self):
        return False

        
    def str(self):
        return self.title