# Generated by Django 4.1.5 on 2023-01-24 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0006_alter_profile_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]