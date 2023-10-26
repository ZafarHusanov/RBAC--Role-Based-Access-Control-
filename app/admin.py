from django.contrib import admin
from .models import Module, Permission, Role, UserRole


class ModuleAdmin(admin.ModelAdmin):
    model = Module
    list_display = ("name",)

admin.site.register(Module ,ModuleAdmin)
admin.site.register(Permission)
admin.site.register(Role)
admin.site.register(UserRole)