# Generated by Django 2.2.14 on 2021-08-06 09:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eduPlatform', '0039_auto_20210806_1439'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogcategory',
            old_name='Category',
            new_name='title',
        ),
    ]
