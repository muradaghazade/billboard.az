from curses.ascii import EM
from django.contrib import admin
from .models import Category, Product, Email, Number

admin.site.register([Category, Email, Number,])

class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ['id','title', 'category', 'code', 'address', 'size', 'retailer', 'retail_price', 'price', 'support_price', 'image',] 
    list_display_links = ('id',)
    list_editable = ['title', 'category', 'size', 'price', 'support_price', 'image',] 

admin.site.register(Product, ProductAdmin)


admin.site.site_header = "Billboard"
admin.site.index_title = "Billboard"
admin.site.site_title = "Billboard Administration"