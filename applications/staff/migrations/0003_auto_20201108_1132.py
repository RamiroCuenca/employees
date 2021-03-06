# Generated by Django 3.1 on 2020-11-08 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0002_auto_20201108_1125'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='staff'),
        ),
        migrations.AddField(
            model_name='staff',
            name='skills',
            field=models.ManyToManyField(to='staff.Skills'),
        ),
    ]
