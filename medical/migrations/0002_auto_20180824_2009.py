# Generated by Django 2.1 on 2018-08-24 17:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medical', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='report',
            name='conditioning_notes',
            field=models.CharField(max_length=225, null=True),
        ),
        migrations.AlterField(
            model_name='report',
            name='injury_comments',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
