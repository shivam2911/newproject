from django.contrib import admin
from .models import Notes

from .models import Items
class NotesAdmin(admin.ModelAdmin):
    list_display =
# Register your models here.
admin.site.register(Notes)
admin.site.register(Items)
