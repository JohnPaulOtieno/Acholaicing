from django.db import models

# Create your models here.

class Cake(models.Model):
    name_of_cake = models.CharField(max_length=200)
    description = models.TextField()
    pricing = models.DecimalField(max_digits=15, decimal_places=2)
    image = models.ImageField(upload_to='offers/', blank=True, null=True)


    def __str__(self):
        return self.name_of_cake


