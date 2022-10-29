from django.contrib import admin
from .models import Bolum, Cihaz, Category
from django.utils.safestring import mark_safe


class CihazAdmin(admin.ModelAdmin):
    list_display =("marka_model","image","description","status","giris_tarihi","cikis_tarihi","SeriNo","selected_categories")
    list_editable=("status","giris_tarihi","cikis_tarihi")
    search_fields= ("marka_model","description","giris_tarihi")
    readonly_fields=("slug",)


    def selected_categories(self,obj):
        html = "<ul>"

        for category in obj.categories.all():
            html+= "<li>" + category.name + "</li>"

        html += "</ul>"
        return mark_safe(html)


admin.site.register(Cihaz,CihazAdmin)
admin.site.register(Category)
admin.site.register(Bolum)



# Register your models here.
