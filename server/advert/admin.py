from django.contrib import admin

from advert.models import Advert

class AdvertAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'description', 'image', 'price', 'author', 'created_date', 'modified_date', 'post_date', 'moderated']
    list_filter = ['title', 'category']
    search_fields = ['title']
    fields = ['title', 'category', 'description', 'image', 'price', 'author', 'moderated']
    readonly_fields = ['id', 'created_date', 'modified_date', 'post_date']


admin.site.register(Advert, AdvertAdmin)



