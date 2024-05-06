from django.db import models

class CategoryBook(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        db_table = 'category'
        app_label = 'book'
    
    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    
    class Meta:
        db_table = 'author'
        app_label = 'book'
        
    def __str__(self):
        return self.name
        
class Publisher(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    
    class Meta:
        db_table = 'publisher'
        app_label = 'book'
        
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='book', blank=True, null=True)
    brand = models.CharField(max_length=50)
    price = models.IntegerField()
    old_price = models.IntegerField()
    description = models.TextField(max_length=1000)
    quantity = models.IntegerField()
    is_active = models.BooleanField()
    is_bestseller = models.BooleanField()
    is_feature = models.BooleanField()
    create_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)
    category = models.ForeignKey(CategoryBook, related_name='books', on_delete=models.CASCADE)
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, related_name='books', on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'book'
        app_label = 'book'