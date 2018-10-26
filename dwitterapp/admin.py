from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Post Details',        {'fields': ['author', 'title', 'text', 'attachment']}),
        ('Date Information',    {'fields': ['create_date'], 'classes': ['collapse']})
    ]

    list_display = ('title', 'text', 'create_date', 'was_published_recently')
    list_filter = ['create_date']
    search_fields = ['title']


admin.site.register(Post, PostAdmin)
