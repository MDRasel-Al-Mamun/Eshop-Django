# Generated by Django 3.0.8 on 2020-08-02 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20200802_1028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='size',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='variants',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
