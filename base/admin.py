from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import Todo
# Register your models here.

@admin.register(Todo)
class Todoadmin(admin.ModelAdmin):
    exclude = ("imgur ", )
    readonly_fields = ('imgur', )

    list_display = ['name', 'want', 'updated_at','show_imgur_url']
    list_display_links = ['name']
    list_per_page = 5
    list_filter = ['name', 'updated_at']
    def show_imgur_url(self, obj):
        return mark_safe('<a href= "%s">사진</a>' % obj.imgur)
    show_imgur_url.allow_tags = True
    show_imgur_url.short_description = '사진링크'
