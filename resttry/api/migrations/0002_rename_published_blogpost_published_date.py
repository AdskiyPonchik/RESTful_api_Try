# Generated by Django 5.0.2 on 2024-02-29 22:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='published',
            new_name='published_date',
        ),
    ]
