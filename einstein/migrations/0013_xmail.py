# Generated by Django 3.2.8 on 2021-10-12 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('einstein', '0012_auto_20211012_2052'),
    ]

    operations = [
        migrations.CreateModel(
            name='Xmail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=95)),
                ('message', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
