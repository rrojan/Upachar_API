# Generated by Django 3.2.3 on 2021-05-24 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210524_1424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='comorbidity_problems',
            field=models.JSONField(),
        ),
        migrations.AlterField(
            model_name='profile',
            name='prevalent_conditions',
            field=models.JSONField(),
        ),
    ]
