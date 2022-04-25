from django.contrib import admin
from .models import Category, Product

admin.site.register([Category,])

class ProductAdmin(admin.ModelAdmin):
    model = Product
    list_display = ['id','title', 'category', 'size', 'price', 'support_price', 'image',] 
    list_display_links = ('id',)
    list_editable = ['title', 'category', 'size', 'price', 'support_price', 'image',] 

admin.site.register(Product, ProductAdmin)


admin.site.site_header = "Billboard"
admin.site.index_title = "Billboard"
admin.site.site_title = "Billboard Administration"