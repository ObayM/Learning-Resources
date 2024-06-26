# Generated by Django 5.0.4 on 2024-04-11 03:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CourseCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.CharField(max_length=100)),
                ('estimated_hours', models.CharField(max_length=100)),
                ('level', models.CharField(max_length=100)),
                ('vote_count', models.CharField(max_length=100)),
                ('vote_average', models.CharField(max_length=100)),
            ],
        ),
    ]
