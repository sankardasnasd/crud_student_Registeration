# Generated by Django 4.0.2 on 2022-12-07 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud_app', '0003_alter_students_student_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='student_phone',
            field=models.BigIntegerField(max_length=12),
        ),
    ]
