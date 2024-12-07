# Generated by Django 4.1.13 on 2024-12-06 10:33

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
                ('rollno', models.IntegerField()),
                ('name', models.CharField(max_length=30)),
                ('dob', models.DateField()),
                ('marks', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('phonenumber', models.CharField(max_length=30)),
                ('address', models.TextField()),
            ],
        ),
    ]