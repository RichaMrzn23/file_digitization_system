# Generated by Django 5.1.4 on 2024-12-28 17:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_user_profile_image_backup_file_filerecovery'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='FileRecovery',
            new_name='Recovery_File',
        ),
    ]