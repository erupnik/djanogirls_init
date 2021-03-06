from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('author','title', 'created_date', 'published_date')
    search_fields = ('title','text')

#admin.site.register(Post)
