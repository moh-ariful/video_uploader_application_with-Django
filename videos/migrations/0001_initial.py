# Generated by Django 3.2.11 on 2022-10-19 01:45

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('video_file', models.FileField(upload_to='uploads/video_files', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4'])])),
                ('thumbnail', models.FileField(upload_to='uploads/thumbnails', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])])),
                ('date_posted', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
