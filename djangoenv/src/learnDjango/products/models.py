from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(blank=True)
    price =models.DecimalField(decimal_places=2,max_digits=10000)
    summary =models.TextField(blank=False, null=False)
    featured =models.BooleanField(default=True)

    def get_absolute_url(self):
        return f"/products/{self.id}/"