# Generated by Django 4.0.3 on 2022-08-16 09:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('become_dealer', '0002_remove_dealer_fullname_dealer_full_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='dealer',
            new_name='become_dealer',
        ),
    ]
