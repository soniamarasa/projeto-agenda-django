from django.contrib import admin
from contact.models import Contact

# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'phone', 'email', 'created_date')
    ordering = ('-id',)
    search_fields = ('first_name', 'last_name', 'phone', 'email')
    list_per_page = 10
    list_editable = ('phone', 'email')
    list_filter = ('created_date',)
    list_display_links = ('id', 'first_name', 'last_name')
