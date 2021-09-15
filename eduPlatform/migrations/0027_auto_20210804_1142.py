# Generated by Django 2.2.14 on 2021-08-04 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eduPlatform', '0026_auto_20210804_1104'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='')),
                ('desc', models.TextField()),
                ('img1', models.ImageField(null=True, upload_to='')),
                ('desc1', models.TextField(null=True)),
                ('img2', models.ImageField(null=True, upload_to='')),
                ('desc2', models.TextField(null=True)),
                ('img3', models.ImageField(null=True, upload_to='')),
                ('desc3', models.TextField(null=True)),
                ('img4', models.ImageField(null=True, upload_to='')),
                ('desc4', models.TextField(null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Blogs',
        ),
    ]
