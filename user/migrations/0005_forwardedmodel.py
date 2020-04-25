# Generated by Django 3.0.5 on 2020-04-25 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20200422_2018'),
    ]

    operations = [
        migrations.CreateModel(
            name='ForwardedModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userd', models.IntegerField(max_length=50)),
                ('category2', models.CharField(max_length=2000)),
                ('title2', models.CharField(max_length=200)),
                ('img2', models.FileField(upload_to='')),
                ('description2', models.CharField(max_length=800)),
                ('location2', models.CharField(max_length=500)),
                ('date2', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]