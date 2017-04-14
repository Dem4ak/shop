from django.contrib import admin
from .models import *


class ProductInOrderInline(admin.TabularInline):
    model = ProductInOrder
    extra = 0


class StatusOrderAdmin(admin.ModelAdmin):
    # list_display = ["name", "email"]
    list_display = [field.name for field in StatusOrder._meta.fields]
    list_filter = ["name"]
    search_fields = ["email"]

    class Meta:
        model = StatusOrder


admin.site.register(StatusOrder, StatusOrderAdmin)


class OrderAdmin(admin.ModelAdmin):
    # list_display = ["name", "email"]
    list_display = [field.name for field in Order._meta.fields]
    inlines = [ProductInOrderInline]

    class Meta:
        model = Order


admin.site.register(Order, OrderAdmin)


class ProductInOrderAdmin(admin.ModelAdmin):
    # list_display = ["name", "email"]
    list_display = [field.name for field in ProductInOrder._meta.fields]

    class Meta:
        model = ProductInOrder


admin.site.register(ProductInOrder, ProductInOrderAdmin)
