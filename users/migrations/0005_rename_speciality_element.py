# Generated by Django 4.0.4 on 2022-08-06 16:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_rename_skill_speciality'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Speciality',
            new_name='Element',
        ),
    ]
