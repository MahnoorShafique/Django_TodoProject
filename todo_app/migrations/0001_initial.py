# Generated by Django 3.2.12 on 2022-10-14 11:44

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('task_name', models.CharField(max_length=50)),
                ('task_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_date', models.DateField(auto_now_add=True)),
                ('due_date', models.DateField()),
                ('updated_date', models.DateField(auto_now=True)),
                ('status', models.CharField(choices=[('pn', 'pending'), ('bl', 'block'), ('dn', 'done')], default='pn', max_length=2)),
                ('description', models.TextField()),
            ],
        ),
    ]
