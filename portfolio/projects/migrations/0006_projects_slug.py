# Generated by Django 4.2.4 on 2023-08-13 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_rename_link_projects_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='slug',
            field=models.SlugField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]
