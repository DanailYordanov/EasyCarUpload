from django.contrib import admin
from .models import Brand, Model, Car, Image


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):

    def brand_models_count(self, obj):
        return obj.model_set.count()

    brand_models_count.short_description = "Model count"
    list_display = ('__str__', 'brand_models_count')


@admin.register(Model)
class asdAdmin(admin.ModelAdmin):

    list_filter = ('brand__brand',)
    list_display = ('__str__', 'brand')


admin.site.register(Car)
admin.site.register(Image)
