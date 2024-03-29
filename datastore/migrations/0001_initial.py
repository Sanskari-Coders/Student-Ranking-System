# Generated by Django 4.2.11 on 2024-03-19 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration_number', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=100)),
                ('department', models.CharField(max_length=100)),
                ('semester', models.IntegerField()),
                ('sgpa', models.FloatField()),
                ('cgpa', models.FloatField()),
            ],
        ),
    ]
