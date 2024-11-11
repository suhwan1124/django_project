from django.contrib import admin
from .models import *

# Register your models here.
# admin.site.register(Post)
# admin.site.register(Comment)
admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Tag)

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['id', 'title']
    ordering = ['title']
    list_filter = ['tag']
    search_fields = ['body']
    list_per_page = 3
    
admin.site.register(Post, PostAdmin)

def make_deleted(modeladmin, request, queryset):
    queryset.update(deleted=True)
    
make_deleted.short_description = '선택된 comments를 삭제상태로 설정합니다.'

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['post', 'author', 'message_length']
    actions = [make_deleted]
    def message_length(self,obj):
        return len(obj.message)
        
    message_length.short_description = '댓글 글자수'