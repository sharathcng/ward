# Generated by Django 3.0.5 on 2020-04-27 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_auto_20200427_1202'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CompletedModel',
        ),
        migrations.AddField(
            model_name='forwardedmodel',
            name='status',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]