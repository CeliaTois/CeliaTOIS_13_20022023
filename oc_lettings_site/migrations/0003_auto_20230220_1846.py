# Generated by Django 3.0 on 2023-02-20 18:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oc_lettings_site', '0002_auto_20230220_1824'),
    ]

    database_operations = [
        migrations.AlterModelTable('Profile', 'profiles_profile'),
    ]

    state_operations = [
        migrations.DeleteModel('Profile'),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=database_operations,
            state_operations=state_operations
        )
    ]
