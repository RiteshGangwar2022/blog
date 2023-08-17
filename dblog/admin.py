from django.contrib import admin
from .models import Category,Post
# Register your models here.

#to show more option to admin

class CategoryAdmin(admin.ModelAdmin):
    list_display =('image_tag','title','description','url','add_date')
    search_fields = ('title',)

class PostAdmin(admin.ModelAdmin):
    list_display = ('image_tag','title','content','cat','add_date')
    search_fields = ('title',)
    list_filter = ('cat',)
    list_per_page =2

admin.site.register(Category,CategoryAdmin)
admin.site.register(Post,PostAdmin)