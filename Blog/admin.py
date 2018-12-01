from django.contrib import admin
from .models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ('title','author','publish_time',"modifies_time")
    list_filter = ('publish_time','author')
    search_fields = ('title','body')
    raw_id_fields = ('author',)
    date_hierarchy = 'publish_time'
    ordering = ['publish_time','author']

admin.site.register(Post,PostAdmin)