# Generated by Django 4.0.2 on 2022-12-07 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='student_phone',
            field=models.TextField(),
        ),
    ]
