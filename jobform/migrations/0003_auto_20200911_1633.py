# Generated by Django 3.1.1 on 2020-09-11 11:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobform', '0002_auto_20200911_1438'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jobform',
            old_name='contactno',
            new_name='contactno2',
        ),
    ]