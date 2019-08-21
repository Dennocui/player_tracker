# Generated by Django 2.1 on 2018-08-23 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='about_player',
            field=models.CharField(max_length=225, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='injury_history',
            field=models.CharField(max_length=225, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='skills',
            field=models.CharField(max_length=225, null=True),
        ),
        migrations.AlterField(
            model_name='player',
            name='tertiary_institution',
            field=models.CharField(max_length=50, null=True),
        ),
    ]