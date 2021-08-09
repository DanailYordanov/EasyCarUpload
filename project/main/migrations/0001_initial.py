# Generated by Django 2.2.22 on 2021-08-09 10:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('', 'Избери'), ('Седан', 'Седан'), ('Хечбек', 'Хечбек'), ('Комби', 'Комби'), ('Купе', 'Купе'), ('Кабрио', 'Кабрио'), ('Джип', 'Джип'), ('Пикап', 'Пикап'), ('Ван', 'Ван')], max_length=10)),
                ('modification', models.CharField(max_length=100)),
                ('engine_type', models.CharField(max_length=20)),
                ('price', models.CharField(max_length=10)),
                ('transmission_type', models.CharField(choices=[('', 'Избери'), ('Автоматични', 'Автоматични'), ('Ръчни', 'Ръчни')], max_length=20)),
                ('fuel_type', models.CharField(choices=[('', 'Избери'), ('Бензин', 'Бензин'), ('Дизел', 'Дизел')], max_length=10)),
                ('power', models.CharField(max_length=5)),
                ('displacement', models.CharField(max_length=5)),
                ('year', models.CharField(max_length=4, verbose_name=[('', 'Избери'), ('1990', '1990'), ('1991', '1991'), ('1992', '1992'), ('1993', '1993'), ('1994', '1994'), ('1995', '1995'), ('1996', '1996'), ('1997', '1997'), ('1998', '1998'), ('1999', '1999'), ('2000', '2000'), ('2001', '2001'), ('2002', '2002'), ('2003', '2003'), ('2004', '2004'), ('2005', '2005'), ('2006', '2006'), ('2007', '2007'), ('2008', '2008'), ('2009', '2009'), ('2010', '2010'), ('2011', '2011'), ('2012', '2012'), ('2013', '2013'), ('2014', '2014'), ('2015', '2015'), ('2016', '2016'), ('2017', '2017'), ('2018', '2018'), ('2019', '2019'), ('2020', '2020'), ('2021', '2021')])),
                ('month', models.CharField(max_length=15, verbose_name=[('', 'Избери'), ('Януари', 'Януари'), ('Февруари', 'Февруари'), ('Март', 'Март'), ('Април', 'Април'), ('Май', 'Май'), ('Юни', 'Юни'), ('Юли', 'Юли'), ('Август', 'Август'), ('Септември', 'Септември'), ('Октомври', 'Октомври'), ('Ноември', 'Ноември'), ('Декември', 'Декември')])),
                ('run', models.CharField(max_length=10)),
                ('color', models.CharField(max_length=20, verbose_name=[('', 'Избери'), ('Бежов', 'Бежов'), ('Бордо', 'Бордо'), ('Бял', 'Бял'), ('Виолетов', 'Виолетов'), ('Жълт', 'Жълт'), ('Зелен', 'Зелен'), ('Кафяв', 'Кафяв'), ('Оранжев', 'Оранжев'), ('Сив', 'Сив'), ('Сребърен', 'Сребърен'), ('Червен', 'Червен'), ('Черен', 'Черен'), ('Лилав', 'Лилав'), ('Розов', 'Розов'), ('Светло зелен', 'Светло зелен'), ('Светло син', 'Светло син'), ('Тъмно зелен', 'Тъмно зелен'), ('Тъмно сив', 'Тъмно сив'), ('Тъмно син', 'Тъмно син')])),
                ('euro_standart', models.CharField(max_length=10, verbose_name=[('', 'Избери'), ('EURO 1', 'EURO 1'), ('EURO 2', 'EURO 2'), ('EURO 3', 'EURO 3'), ('EURO 4', 'EURO 4'), ('EURO 5', 'EURO 5'), ('EURO 6', 'EURO 6')])),
                ('description', models.CharField(max_length=400)),
                ('brand', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Brand')),
            ],
        ),
        migrations.CreateModel(
            name='Model',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=50)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Brand')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='car_pics')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Car')),
            ],
        ),
        migrations.AddField(
            model_name='car',
            name='model',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.Model'),
        ),
        migrations.AddField(
            model_name='car',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
