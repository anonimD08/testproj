# Generated by Django 2.1 on 2018-09-11 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monitor', '0004_auto_20180911_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='description',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]