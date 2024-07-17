from django.db import models
    
    
class ProductCategory(models.Model):
    id=models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.name
class Product(models.Model):    
    id=models.BigAutoField(primary_key=True)
    title=models.CharField(max_length=60)
    description=models.TextField(max_length=120)
    size=models.CharField(max_length=60)
    color=models.CharField(max_length=60)
    category=models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    price=models.CharField(max_length=10)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    class Meta:
        unique_together = [['title', 'color']]  
    def __str__(self):
        return self.title