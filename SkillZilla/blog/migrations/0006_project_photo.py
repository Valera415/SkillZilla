# Generated by Django 4.2.7 on 2024-01-07 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_remove_project_photo_remove_project_slug_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='photo',
            field=models.ImageField(default='asd', upload_to='photos/'),
            preserve_default=False,
        ),
    ]
