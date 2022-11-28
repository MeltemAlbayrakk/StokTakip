from django.contrib import admin
from .models import Departments, Categories, Devices, Employees, Status
from django.utils.safestring import mark_safe


class DevicesAdmin(admin.ModelAdmin):
    list_display = (
        "brand",
        "description",
        "status",
        "arrival_date",
        "exit_date",
        "selected_categories",
    )
    list_editable = ("status", "arrival_date", "exit_date")
    search_fields = ("brand", "description")

    def selected_categories(self, obj):
        html = "<ul>"

        html += "<li>" + obj.category.name + "</li>"

        html += "</ul>"
        return mark_safe(html)


admin.site.register(Devices, DevicesAdmin)
admin.site.register(Categories)
admin.site.register(Departments)
admin.site.register(Employees)
admin.site.register(Status)


# Register your models here.
