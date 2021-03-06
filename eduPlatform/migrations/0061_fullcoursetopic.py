# Generated by Django 2.2.14 on 2021-08-31 05:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eduPlatform', '0060_auto_20210825_1725'),
    ]

    operations = [
        migrations.CreateModel(
            name='FullCourseTopic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=500)),
                ('duration_in_hours', models.IntegerField()),
                ('class_link', models.CharField(blank=True, max_length=1000, null=True)),
                ('lecture_video', models.FileField(blank=True, null=True, upload_to='courseTutorials/')),
                ('full_course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eduPlatform.FullCourse')),
            ],
        ),
    ]
