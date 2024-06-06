from django.contrib import admin
from  .models import FoodType, Food, Comment

# Register your models here.


class FoodTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('name',)


class FoodAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')
    list_display_links = ('name',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'text', 'created')
    list_display_links = ('author',)


admin.site.register(FoodType, FoodTypeAdmin)
admin.site.register(Food, FoodAdmin)
admin.site.register(Comment, CommentAdmin)