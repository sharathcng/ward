# Generated by Django 3.0.5 on 2020-04-26 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_completedmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='completedmodel',
            name='comp_id',
            field=models.IntegerField(max_length=50),
        ),
    ]