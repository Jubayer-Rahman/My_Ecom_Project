# Generated by Django 3.2.4 on 2021-07-04 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App_Payment', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='billingadress',
            old_name='adress',
            new_name='address',
        ),
    ]
