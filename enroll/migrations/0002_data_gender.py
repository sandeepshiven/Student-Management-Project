# Generated by Django 2.0.2 on 2019-11-30 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='data',
            name='Gender',
            field=models.CharField(max_length=10),

        ),
    ]
