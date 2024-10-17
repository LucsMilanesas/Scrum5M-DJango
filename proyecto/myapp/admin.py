# Register your models here.
from django.contrib import admin
from .models import Marca, Producto

class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre","precio","stock","nuevo", "marca"]
    list_editable = ["precio",]
    search_fields = ["nombre"]
    list_filter = ["marca"]
    #list_per_page = 1

admin.site.register(Marca)
admin.site.register(Producto,ProductoAdmin)
