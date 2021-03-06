# Generated by Django 3.1 on 2020-11-08 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=50, verbose_name='Skill')),
            ],
            options={
                'verbose_name': 'Skill',
                'verbose_name_plural': 'Skills',
            },
        ),
        migrations.AlterModelOptions(
            name='staff',
            options={'ordering': ['job'], 'verbose_name': 'Worker', 'verbose_name_plural': 'Staff'},
        ),
        migrations.AlterUniqueTogether(
            name='staff',
            unique_together={('first_name', 'last_name')},
        ),
    ]
