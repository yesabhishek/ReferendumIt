# Generated by Django 3.0.8 on 2021-06-06 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0011_remove_profile_mobile'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='mobile',
            field=models.CharField(blank=True, max_length=10, null=True, unique=True),
        ),
    ]
