# Generated by Django 3.0.8 on 2021-06-06 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0013_auto_20210606_1941'),
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Petition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agenda', models.CharField(blank=True, max_length=500, null=True)),
                ('choice', models.CharField(blank=True, choices=[('Y', 'Yes'), ('N', 'No'), ('Nu', 'None')], max_length=50, null=True, verbose_name='Choice')),
                ('created_on', models.DateField(auto_now_add=True, verbose_name='Created On')),
                ('status', models.CharField(blank=True, choices=[('A', 'Active'), ('X', 'End'), ('W', 'Waiting')], max_length=1, null=True, verbose_name='Status')),
                ('ends_on', models.DateField(blank=True, null=True, verbose_name='Deadline')),
                ('updated_on', models.DateField(auto_now_add=True, verbose_name='Updated On')),
                ('voter', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.Profile')),
            ],
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
