# Generated by Django 3.0.5 on 2020-04-22 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('N_title', models.CharField(max_length=200)),
                ('N_img', models.FileField(blank=True, null=True, upload_to='')),
                ('N_description', models.CharField(max_length=800)),
                ('N_date', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
