# Generated by Django 4.1.1 on 2022-10-27 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Contest', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CreatedContest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contest_id', models.CharField(max_length=100)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('first', models.CharField(max_length=100)),
                ('second', models.CharField(max_length=100)),
                ('third', models.CharField(max_length=100)),
                ('forth', models.CharField(max_length=100)),
                ('start_time', models.DateTimeField(auto_now_add=True)),
                ('end_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
    ]
