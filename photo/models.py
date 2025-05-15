from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100,blank=True)

    def __str__(self):
        return self.name
    
class Photo(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, blank=True,)
    image = models.ImageField(upload_to='photos/')
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title
