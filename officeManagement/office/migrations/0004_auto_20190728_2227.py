# Generated by Django 2.0 on 2019-07-28 21:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0003_staff_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='status',
            field=models.CharField(default='No', max_length=3),
        ),
        migrations.AlterField(
            model_name='staff',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
