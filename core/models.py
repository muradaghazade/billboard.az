from django.db import models
import random

class Product(models.Model):
    title = models.CharField(max_length=200)
    code = models.CharField(max_length=50, blank=True)
    size = models.DecimalField('Size',max_digits=6, decimal_places=2)
    price = models.DecimalField('Price',max_digits=6, decimal_places=2)
    support_price = models.DecimalField('Support Price',max_digits=6, decimal_places=2)
    image = models.ImageField('Image',upload_to='images/', null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, db_index=True, related_name='products', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
        
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def save(self, *args, **kwargs):
        num_list = [i for i in range(10)]
        code_items = []

        for i in range(6):
            num = random.choice(num_list)
            code_items.append(num)

        code = "".join(str(item) for item in code_items)
        self.code = f'{code}'
        super(Product, self).save(*args, **kwargs)


class Category(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title
        
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
