# Generated by Django 4.2 on 2023-05-03 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_api', '0003_rename_path_id_student_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]