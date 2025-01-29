from django.db import models
import datetime

# Create your models here.

class category(models.Model):
  name = models.CharField(max_length=50)

  def __str__(self):
    return self.name
  

# product model.
class product(models.Model):
    name = models.CharField(max_length=255, unique=True)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    category = models.ForeignKey(category, on_delete=models.CASCADE, default=1)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='products/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
    def create_product(cls, name, description='', image=None):
        product= cls.objects.create(
            name=name,
            description=description,
            image=image
        )
        return product

    
    @classmethod
    def update_product(cls, product_id, name=None, description=None, image=None):
        
        try:
            product = cls.objects.get(id=product_id)  
            if name:
              product.name = name  
            if description:
                product.description = description  
            if image:
                product.image = image  
            product.save()  
            return product
        except cls.DoesNotExist:
            return None  

    
    @classmethod
    def list_product(cls):
        
        return cls.objects.all()  

    
    @classmethod
    def retrieve_product(cls, product_id):
        
        try:
            product = cls.objects.get(id=product_id)  
            return  product
        except cls.DoesNotExist:
            return None  

    
    @classmethod
    def delete_product(cls, product_id):
        
        try:
            product = cls.objects.get(id=product_id)  
            product.delete()  
            return True  
        except cls.DoesNotExist:
            return False  