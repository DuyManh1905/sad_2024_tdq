from django.db import models

class CategoryMobile(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'category'
        app_label = 'mobile'
        
    def __str__(self):
        return self.name

class Mobile(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='book', blank=True, null=True)
    brand = models.CharField(max_length=50)
    price = models.IntegerField()
    old_price = models.IntegerField()
    description = models.TextField(max_length=1000)
    quantity = models.IntegerField()
    is_active = models.BooleanField()
    is_bestseller = models.BooleanField()
    is_feature = models.BooleanField()
    create_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(CategoryMobile, related_name='mobies', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'mobile'
        app_label = 'mobile'