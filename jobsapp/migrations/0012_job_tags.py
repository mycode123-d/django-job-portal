# Generated by Django 3.0.7 on 2020-11-26 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0001_initial'),
        ('jobsapp', '0011_auto_20201118_1751'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='tags',
            field=models.ManyToManyField(to='tags.Tag'),
        ),
    ]
