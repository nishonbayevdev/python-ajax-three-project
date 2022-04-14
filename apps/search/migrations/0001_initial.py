# Generated by Django 4.0 on 2022-03-25 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SearchModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Sarlavha')),
                ('text', models.TextField(verbose_name='Matn')),
                ('createData', models.DateTimeField(verbose_name='Vaqt')),
            ],
            options={
                'verbose_name_plural': 'Qidiruv',
            },
        ),
    ]
