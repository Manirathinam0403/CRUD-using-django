# Generated by Django 4.1.3 on 2023-07-31 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registerId', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('age', models.IntegerField()),
                ('course', models.CharField(max_length=255)),
                ('CGPA', models.IntegerField()),
            ],
        ),
    ]