# Generated by Django 2.2.14 on 2021-08-25 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eduPlatform', '0054_event_post_views'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='iamge_speakerm',
            field=models.ImageField(blank=True, null=True, upload_to='event_speakers/'),
        ),
    ]