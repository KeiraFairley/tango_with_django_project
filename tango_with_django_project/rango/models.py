from django.db import models
DEFAULT=0
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = DEFAULT
    likes = DEFAULT
    
def __str__(self):
    return self.name

class Page(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title