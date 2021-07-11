# Generated by Django 3.2.4 on 2021-07-10 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('address', models.CharField(max_length=122)),
                ('types', models.CharField(max_length=122)),
                ('quantity', models.CharField(max_length=122)),
                ('location', models.CharField(max_length=122)),
                ('description', models.TextField()),
            ],
        ),
    ]
