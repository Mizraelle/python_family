from django.contrib import admin
from .models import Video, Comment

class VideoInline(admin.StackedInline):
    model = Comment
    extra = 2
    readonly_fields = ['likes']

class VideoAdmin(admin.ModelAdmin):
    inlines = [VideoInline]
    readonly_fields = ['likes_video']
    list_filter = ['date_video']
    list_display = ['name_video', 'videoplay']
    prepopulated_fields = {'name_video':["slug"]}


admin.site.register(Video, VideoAdmin)
# Register your models here.
