# Generated by Django 3.0.5 on 2020-04-22 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20200422_2007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='N_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='post_complaint',
            name='date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
