# Generated by Django 3.0.5 on 2020-04-27 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_auto_20200426_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='completedmodel',
            name='comp_id',
            field=models.BigIntegerField(max_length=50),
        ),
    ]
