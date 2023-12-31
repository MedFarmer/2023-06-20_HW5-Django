# Generated by Django 4.2.2 on 2023-06-20 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_address', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Desciption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_description', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Names',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hotel_name', models.CharField(max_length=50)),
            ],
        ),
    ]
