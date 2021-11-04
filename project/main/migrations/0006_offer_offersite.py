# Generated by Django 2.2.22 on 2021-11-04 16:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20211022_1524'),
    ]

    operations = [
        migrations.CreateModel(
            name='OfferSite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('site_url', models.URLField(max_length=100)),
                ('offer_url', models.URLField(max_length=100)),
                ('delete_url', models.URLField(max_length=100)),
                ('create_url', models.URLField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offer_id', models.CharField(max_length=50)),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Car')),
                ('site', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.OfferSite')),
            ],
        ),
    ]