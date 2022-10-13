# Generated by Django 3.2.12 on 2022-10-13 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='status',
            field=models.CharField(choices=[('PN', 'pending'), ('PR', 'inProgress'), ('BL', 'blocked'), ('DN', 'done')], default='PN', max_length=70),
        ),
    ]
