# Generated by Django 3.2.4 on 2021-06-19 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Login', '0002_auto_20210619_2331'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='full_name',
            field=models.CharField(blank=True, max_length=264),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
