from django.db import models
from django.conf import settings
import django.utils.timezone as timezone
from .scripts.cars_bg import CarsBgClass


TRANSMISSION_TYPE_CHOICES = [
    ('', 'Избери'),
    ('Автоматични', 'Автоматични'),
    ('Ръчни', 'Ръчни')
]

CATEGORY_CHOICES = [
    ('', 'Избери'),
    ('Седан', 'Седан'),
    ('Хечбек', 'Хечбек'),
    ('Комби', 'Комби'),
    ('Купе', 'Купе'),
    ('Кабрио', 'Кабрио'),
    ('Джип', 'Джип'),
    ('Пикап', 'Пикап'),
    ('Ван', 'Ван')
]

FUEL_TYPE_CHOICES = [
    ('', 'Избери'),
    ('Бензин', 'Бензин'),
    ('Дизел', 'Дизел')
]

YEAR_CHOICES = [
    ('', 'Избери'),
]

MONTH_CHOICES = [
    ('', 'Избери'),
    ('Януари', 'Януари'),
    ('Февруари', 'Февруари'),
    ('Март', 'Март'),
    ('Април', 'Април'),
    ('Май', 'Май'),
    ('Юни', 'Юни'),
    ('Юли', 'Юли'),
    ('Август', 'Август'),
    ('Септември', 'Септември'),
    ('Октомври', 'Октомври'),
    ('Ноември', 'Ноември'),
    ('Декември', 'Декември')
]

DOORS_TYPE_CHOICES = [
    ('', 'Избери'),
    ('2/3', '2/3'),
    ('4/5', '4/5')
]

COLOR_CHOICES = [
    ('', 'Избери'),
    ('Бежов', 'Бежов'),
    ('Бордо', 'Бордо'),
    ('Бял', 'Бял'),
    ('Виолетов', 'Виолетов'),
    ('Жълт', 'Жълт'),
    ('Зелен', 'Зелен'),
    ('Кафяв', 'Кафяв'),
    ('Оранжев', 'Оранжев'),
    ('Сив', 'Сив'),
    ('Сребърен', 'Сребърен'),
    ('Червен', 'Червен'),
    ('Черен', 'Черен'),
    ('Лилав', 'Лилав'),
    ('Розов', 'Розов'),
    ('Светло зелен', 'Светло зелен'),
    ('Светло син', 'Светло син'),
    ('Тъмно зелен', 'Тъмно зелен'),
    ('Тъмно сив', 'Тъмно сив'),
    ('Тъмно син', 'Тъмно син')
]

EURO_STANDART_CHOICES = [
    ('', 'Избери'),
    ('EURO 1', 'EURO 1'),
    ('EURO 2', 'EURO 2'),
    ('EURO 3', 'EURO 3'),
    ('EURO 4', 'EURO 4'),
    ('EURO 5', 'EURO 5'),
    ('EURO 6', 'EURO 6')
]


def create_year_choices(from_year, to_year):
    for year in range(from_year, to_year):
        YEAR_CHOICES.append((str(year), str(year)))


current_year = timezone.now().year
create_year_choices(1990, current_year + 1)


class Brand(models.Model):
    brand = models.CharField(max_length=50)

    def __str__(self):
        return self.brand


class Model(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    model = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.brand} - {self.model}'


class Car(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    category = models.CharField(
        choices=CATEGORY_CHOICES, max_length=10)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True)
    model = models.ForeignKey(Model, on_delete=models.SET_NULL, null=True)
    modification = models.CharField(max_length=100)
    engine_type = models.CharField(max_length=20)
    price = models.IntegerField()
    transmission_type = models.CharField(
        choices=TRANSMISSION_TYPE_CHOICES, max_length=20)
    fuel_type = models.CharField(
        choices=FUEL_TYPE_CHOICES, max_length=10)
    doors_type = models.CharField(choices=DOORS_TYPE_CHOICES, max_length=5)
    power = models.IntegerField()
    displacement = models.IntegerField()
    year = models.CharField(choices=YEAR_CHOICES, max_length=4)
    month = models.CharField(choices=MONTH_CHOICES, max_length=15)
    run = models.IntegerField()
    color = models.CharField(choices=COLOR_CHOICES, max_length=20)
    euro_standart = models.CharField(
        choices=EURO_STANDART_CHOICES, max_length=10)
    description = models.CharField(max_length=400)

    def __str__(self):
        return f'{self.brand} {self.model} - {self.price}лв.'

    def get_image_paths(self):
        images = self.image_set.all()
        image_paths = []

        for image in images:
            image_paths.append(image.image.path)

        return image_paths


class Image(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='car_pics')

    def __str__(self):
        return f'{self.car.brand} - {self.car.model} - {self.car.modification} - {self.car.price}'


class OfferSite(models.Model):
    name = models.CharField(max_length=50)
    site_url = models.URLField(max_length=100)
    offer_url = models.URLField(max_length=100)
    delete_url = models.URLField(max_length=100)
    create_url = models.URLField(max_length=100)

    def __str__(self):
        return self.name


class Offer(models.Model):
    offer_id = models.CharField(max_length=50)
    site = models.ForeignKey(OfferSite, on_delete=models.SET_NULL, null=True)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.car.brand} - {self.car.model} - {self.car.modification} - {self.car.price}'
