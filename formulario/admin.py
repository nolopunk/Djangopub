# admin.py
from django.contrib import admin
from .models import Contacto

class ContactoAdmin(admin.ModelAdmin):
    # Fields to display in the list view
    list_display = ('nombres', 'apellidos', 'rut', 'email', 'telefono', 'reg_date')

    # Fields that can be searched
    search_fields = ('nombres', 'apellidos', 'rut', 'email')

    # Fields that can be filtered by in the admin list view
    list_filter = ('comuna', 'reg_date')

    # Fields that are displayed in detail/edit view as read-only (optional)
    readonly_fields = ('reg_date',)

    # Fieldsets allow organizing the fields in the form
    fieldsets = (
        (None, {
            'fields': ('nombres', 'apellidos', 'rut', 'email', 'direccion', 'comuna', 'telefono', 'mensaje')
        }),
        ('Metadata', {
            'fields': ('reg_date',),
        }),
    )

admin.site.register(Contacto, ContactoAdmin)
