# Generated by Django 2.0 on 2019-07-28 21:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0005_auto_20190728_2230'),
    ]

    operations = [
        migrations.RenameField(
            model_name='staff',
            old_name='resumption_date',
            new_name='resumtion_date',
        ),
    ]