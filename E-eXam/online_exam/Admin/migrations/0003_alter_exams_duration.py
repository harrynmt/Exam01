# Generated by Django 5.0.3 on 2024-03-30 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0002_exams_duration_exams_passing_score_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exams',
            name='duration',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
