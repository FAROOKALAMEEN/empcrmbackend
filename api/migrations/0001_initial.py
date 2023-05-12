# Generated by Django 4.1.7 on 2023-05-11 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('department', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('salary', models.PositiveIntegerField()),
            ],
        ),
    ]
