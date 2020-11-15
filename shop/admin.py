from django.contrib import admin
from shop.models import  Product,ProductImage




class ProductImageModel(admin.StackedInline):
    model = ProductImage

class ProductModel(admin.ModelAdmin):
    list_display = ['id', 'name', 'get_description', 'get_price', 'get_discount']
    inlines = [ProductImageModel];
    def get_description(self, obj):
        return obj.description[0:5]

    def get_price(self,obj):
        return obj.price

    def get_discount(self,obj):
        return obj.discount

    #get_price.short_description =


# Register your models here.
#admin.site.register(ProductImage, ProductImageModel)
admin.site.register(Product, ProductModel)

