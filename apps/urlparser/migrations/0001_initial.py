# Generated by Django 4.0 on 2022-03-23 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UrlParser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=1024)),
                ('uuid', models.CharField(max_length=1024)),
            ],
            options={
                'verbose_name_plural': 'Url parser',
            },
        ),
    ]