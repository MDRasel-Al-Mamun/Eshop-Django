from django.contrib import admin
from . models import ShopCart
from . models import ShopCart, Order, OrderProduct

class ShopCartAdmin(admin.ModelAdmin):
    list_display = ['product', 'user', 'quantity', 'price', 'amount']
    list_filter = ['user']

    class Meta:
        model = ShopCart

admin.site.register(ShopCart, ShopCartAdmin)


class OrderProductline(admin.TabularInline):
    model = OrderProduct
    readonly_fields = ('user', 'product', 'price', 'quantity', 'amount')
    can_delete = False
    extra = 0


class OrderAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'phone', 'city', 'total', 'status']
    list_filter = ['status']
    readonly_fields = ('user', 'address', 'country', 'phone', 'first_name', 'ip', 'last_name', 'city', 'total')
    can_delete = False
    inlines = [OrderProductline]

    class Meta:
        model = Order


admin.site.register(Order, OrderAdmin)


class OrderProductAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'price', 'quantity', 'amount']
    list_filter = ['user']

    class Meta:
        model = OrderProduct


admin.site.register(OrderProduct, OrderProductAdmin)
