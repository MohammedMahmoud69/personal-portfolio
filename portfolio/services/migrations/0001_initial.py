# Generated by Django 4.2.4 on 2023-08-13 06:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('describtion', models.TextField()),
                ('icon', models.ImageField(upload_to='media/services')),
            ],
            options={
                'verbose_name_plural': 'Services',
            },
        ),
    ]
