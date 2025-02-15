# Generated by Django 5.1.5 on 2025-02-08 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0002_rename_name_repository_authornames_repository_title_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repository',
            name='authorNames',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='repository',
            name='title',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='repository',
            name='url',
            field=models.URLField(max_length=255),
        ),
    ]
