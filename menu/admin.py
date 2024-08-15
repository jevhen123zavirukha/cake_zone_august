from django.contrib import admin
from .models import Dish, Category
from django.utils.safestring import mark_safe


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'is_visible')
    list_filter = ('is_visible', )


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    list_display = ('photo_tag', 'name', 'price', 'is_visible')
    list_filter = ('is_visible', )
    search_fields = ('name', 'position')
    list_editable = ('name', 'is_visible')

    def photo_tag(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50"  height="50"/>')

    photo_tag.short_description = 'Photo'
