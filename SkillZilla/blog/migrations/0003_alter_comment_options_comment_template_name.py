# Generated by Django 4.2.7 on 2023-11-27 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment_created_at'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created_at']},
        ),
        migrations.AddField(
            model_name='comment',
            name='template_name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
