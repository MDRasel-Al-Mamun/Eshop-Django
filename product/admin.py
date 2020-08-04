import admin_thumbnails
from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from . models import *


class CategoryAdminMptt(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title', 'related_products_count', 'related_products_cumulative_count')
    list_display_links = ('indented_title',)
    search_fields = ['__str__', 'title']
    prepopulated_fields = {'slug': ('title',)}
    list_per_page = 10

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        qs = Category.objects.add_related_count(qs, Product, 'category', 'products_cumulative_count', cumulative=True)

        qs = Category.objects.add_related_count(qs, Product, 'category', 'products_count', cumulative=False)
        return qs

    def related_products_count(self, instance):
        return instance.products_count
    related_products_count.short_description = 'Related products (for this specific category)'

    def related_products_cumulative_count(self, instance):
        return instance.products_cumulative_count
    related_products_cumulative_count.short_description = 'Related products (in tree)'


admin.site.register(Category, CategoryAdminMptt)


@admin_thumbnails.thumbnail('image')
class ProductImageInline(admin.TabularInline):
    model = Images
    readonly_fields = ('id',)
    extra = 2


class ProductVariantsInline(admin.TabularInline):
    model = Variants
    readonly_fields = ('image_tag',)
    extra = 1
    show_change_link = True


class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'category', 'status', 'image_tag']
    search_fields = ['__str__', 'price']
    list_filter = ['category']
    readonly_fields = ['image_tag']
    inlines = [ProductImageInline, ProductVariantsInline]
    prepopulated_fields = {'slug': ('title',)}
    list_per_page = 10

    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)


@admin_thumbnails.thumbnail('image')
class ImagesAdmin(admin.ModelAdmin):
    list_display = ['image', '__str__', 'image_thumbnail']
    search_fields = ['__str__']

    class Meta:
        model = Images


admin.site.register(Images, ImagesAdmin)


class CommentAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'comment', 'status', 'create_at']
    list_filter = ['status']
    readonly_fields = ('__str__', 'comment', 'subject', 'ip', 'user', 'product', 'rate', 'id')

    class Meta:
        model = Comment

admin.site.register(Comment, CommentAdmin)


class ColorAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'code', 'color_tag']
    search_fields = ['__str__']


admin.site.register(Color, ColorAdmin)


class SizeAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'code']


admin.site.register(Size, SizeAdmin)


class VariantsAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'product', 'color', 'size', 'price', 'quantity', 'image_tag']
    search_fields = ['__str__']
    list_filter = ['product']


admin.site.register(Variants, VariantsAdmin)
