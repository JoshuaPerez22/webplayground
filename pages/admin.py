from django.contrib import admin
from .models import Page, NotificationConfig

# Register your models here.


class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')

    class Media:
        css = {
            'all': ('pages/css/custom_ckeditor.css',)
        }

class NotificationConfigAdmin(admin.ModelAdmin):
    list_display = ('name', 'day')



admin.site.register(Page, PageAdmin)
admin.site.register(NotificationConfig, NotificationConfigAdmin)
