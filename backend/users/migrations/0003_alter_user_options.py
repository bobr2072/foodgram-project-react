# Generated by Django 3.2.18 on 2023-03-22 12:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20230320_2020'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ('id',), 'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
    ]
