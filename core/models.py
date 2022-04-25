from django.db import models
import random

class Product(models.Model):
    title = models.CharField('Ad', max_length=200)
    code = models.CharField('Kod', max_length=50, blank=True)
    size = models.CharField('Ölcu', max_length=200)
    address = models.CharField('Ünvan', max_length=5000)
    retailer = models.CharField('Tədarükcü', max_length=500)
    retail_price = models.DecimalField('Alış Qiyməti',max_digits=6, decimal_places=2)
    price = models.DecimalField('Qiymət',max_digits=6, decimal_places=2)
    support_price = models.DecimalField('Qurlaşdirma Qiyməti',max_digits=6, decimal_places=2)
    image = models.ImageField('Şəkil',upload_to='images/', null=True, blank=True)
    category = models.ForeignKey('Kateqoriya', on_delete=models.CASCADE, db_index=True, related_name='products', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
        
    class Meta:
        verbose_name = 'Məhsul'
        verbose_name_plural = 'Məhsullar'

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
        verbose_name = 'Kateqoriya'
        verbose_name_plural = 'Kateqoriyalar'


class Email(models.Model):
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.email
        
    class Meta:
        verbose_name = 'Email'
        verbose_name_plural = 'Emaillar'


class Number(models.Model):
    number = models.CharField(max_length=200)

    def __str__(self):
        return self.number
        
    class Meta:
        verbose_name = 'Nomre'
        verbose_name_plural = 'Nomreler'
