# Generated by Django 4.2.4 on 2023-08-14 11:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_emails_options'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Emails',
        ),
    ]
