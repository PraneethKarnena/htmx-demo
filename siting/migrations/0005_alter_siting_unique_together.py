# Generated by Django 3.2.13 on 2022-06-07 12:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('siting', '0004_auto_20220607_1747'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='siting',
            unique_together={('breed', 'date')},
        ),
    ]