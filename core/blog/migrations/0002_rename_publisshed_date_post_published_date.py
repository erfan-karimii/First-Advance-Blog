# Generated by Django 4.1.2 on 2022-11-20 08:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='publisshed_date',
            new_name='published_date',
        ),
    ]
