# Generated by Django 3.0.8 on 2020-07-28 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0002_auto_20200726_1604'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='address',
            new_name='Address',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='dob',
            new_name='Dob',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='f_name',
            new_name='First_name',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='p_no',
            new_name='P_no',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='l_name',
            new_name='last_name',
        ),
    ]