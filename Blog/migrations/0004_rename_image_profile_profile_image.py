# Generated by Django 4.1.5 on 2023-01-24 14:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0003_profile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='image',
            new_name='profile_image',
        ),
    ]
