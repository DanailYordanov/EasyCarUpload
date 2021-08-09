from django.core.management.base import BaseCommand
from main.scripts.mobile_bg import MobileBgClass
from main.models import Brand, Model


class Command(BaseCommand):
    help = 'Import brands and models from mobile.bg'

    def handle(self, *args, **kwargs):
        instance = MobileBgClass()
        data = instance.export_brands()

        for brand, models in data.items():
            brand_object = Brand.objects.create(brand=brand)
            for model in models:
                model_object = Model.objects.create(
                    brand=brand_object, model=model)
