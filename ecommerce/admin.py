from django.contrib import admin
from .models import *
from django.utils.html import format_html
class Admincategory(admin.ModelAdmin):
    

    search_fields=['title','id']

    def delete_button(self,obj):
        return format_html('<a href="/admin/shop/category/{}/delete">delete</a>',obj.id)
    
    def update_button(self,obj):
        return format_html('<a href="/admin/shop/category/{}/change">update</a>',obj.id)
    


    list_display=['id','title','slug','description','delete_button','update_button']
    list_display_links=['title','slug']
    prepopulated_fields ={'slug':('title',)}


class Products(admin.ModelAdmin):


    def delete(self,obj):
        return format_html('<a href="/admin/shop/product/{}/delete">delete</a>',obj.id)
    
    def update(self,obj):
        return format_html('<a href="/admin/shop/product/{}/change" class="bg-green">up</a>',obj.id)

    search_fields=['name','brand']
    list_display_links=['name','brand']
    list_display=['id','name','image','price','discount_price','brand','delete','update']
    prepopulated_fields={'slug':('name',)}
admin.site.register(Category,Admincategory)

admin.site.register(Product,Products)
admin.site.register(Order)
admin.site.register(Coupon)