# Generated by Django 3.1.1 on 2020-09-14 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobform', '0005_auto_20200914_1246'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobform',
            name='aadharform',
            field=models.FileField(blank=True, upload_to='documents'),
        ),
        migrations.AddField(
            model_name='jobform',
            name='drivinglicenseform',
            field=models.FileField(blank=True, upload_to='documents'),
        ),
        migrations.AddField(
            model_name='jobform',
            name='vehicleinsform',
            field=models.FileField(blank=True, upload_to='documents'),
        ),
        migrations.AddField(
            model_name='jobform',
            name='vehicleregform',
            field=models.FileField(blank=True, upload_to='documents'),
        ),
    ]