# Generated by Django 4.2.7 on 2023-11-27 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_alter_comment_options_comment_template_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='template_name',
        ),
        migrations.AddField(
            model_name='project',
            name='template_name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
