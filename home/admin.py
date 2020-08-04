from django.contrib import admin
from .models import *

class SettingtAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'company', 'status']
    search_fields = ['__str__', 'company']
    list_filter = ['company']
    list_per_page = 10

    class Meta:
        model = Setting

admin.site.register(Setting, SettingtAdmin)


class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'subject', 'update_at', 'status']
    readonly_fields = ('__str__', 'subject', 'email', 'message', 'ip')
    search_fields = ['__str__', 'subject']
    list_filter = ['status']
    list_per_page = 10

    class Meta:
        model = ContactMessage

admin.site.register(ContactMessage, ContactMessageAdmin)


class FAQAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'ordernumber', 'status']
    list_filter = ['status']
    search_fields = ['__str__']
    list_per_page = 10

    class Meta:
        model = FAQ


admin.site.register(FAQ, FAQAdmin)
