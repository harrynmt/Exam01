# Generated by Django 5.0.3 on 2024-04-01 05:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0004_examsattended'),
        ('register_login', '0002_studentdetails_image'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ExamsAttended',
            new_name='ExamsResults',
        ),
    ]
