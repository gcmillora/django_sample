# Generated by Django 5.1.5 on 2025-02-08 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='repository',
            old_name='name',
            new_name='authorNames',
        ),
        migrations.AddField(
            model_name='repository',
            name='title',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='repository',
            name='url',
            field=models.URLField(default='', max_length=255),
        ),
    ]
