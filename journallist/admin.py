from django.contrib import admin

from models import JLCategory, JLItem

class CategoryAdmin(admin.ModelAdmin):
    exclude = ('slug',)


class ItemAdmin(admin.ModelAdmin):
    pass

admin.site.register(JLCategory, CategoryAdmin)
admin.site.register(JLItem, ItemAdmin)
