# Generated by Django 2.2.14 on 2021-08-04 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eduPlatform', '0031_remove_blog_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='title',
            field=models.CharField(default='Un-Named', max_length=40),
        ),
    ]
