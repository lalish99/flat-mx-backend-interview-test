# Generated by Django 3.2.9 on 2021-11-23 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('git_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pullrequest',
            name='author',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='pullrequest',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
