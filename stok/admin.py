from django.contrib import admin
from .models import Stok,Category


class StokAdmin(admin.ModelAdmin):
    list_display =("title","is_active","is_home","slug")
    list_editable=("is_active","is_home")
    search_fields= ("title","description")
    readonly_fields=("slug",)


admin.site.register(Stok,StokAdmin)
admin.site.register(Category)

# Register your models here.
