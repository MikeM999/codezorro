# Generated by Django 3.2.7 on 2021-09-16 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('einstein', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appuser',
            name='address',
            field=models.CharField(default=12, max_length=200),
            preserve_default=False,
        ),
    ]
