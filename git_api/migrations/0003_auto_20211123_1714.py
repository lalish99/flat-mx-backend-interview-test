# Generated by Django 3.2.9 on 2021-11-23 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('git_api', '0002_auto_20211123_1229'),
    ]

    operations = [
        migrations.AddField(
            model_name='pullrequest',
            name='base_branch',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='pullrequest',
            name='rebase_branch',
            field=models.CharField(blank=True, default=None, max_length=255, null=True),
        ),
    ]
