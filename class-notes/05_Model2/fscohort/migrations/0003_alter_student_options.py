# Generated by Django 4.2 on 2023-04-25 10:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fscohort', '0002_student_avatar_student_is_active_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ('-number',), 'verbose_name': 'Ogrenci', 'verbose_name_plural': 'ogrenciler'},
        ),
    ]
