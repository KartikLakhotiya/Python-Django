# Generated by Django 5.0.1 on 2024-01-13 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CourseName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseTitle', models.CharField(max_length=50)),
                ('coursePrice', models.IntegerField()),
                ('courseHeading', models.CharField(max_length=100)),
                ('courseDesc', models.TextField()),
                ('trainerName', models.CharField(max_length=50)),
                ('presentStudent', models.IntegerField()),
                ('studentLikes', models.IntegerField()),
            ],
        ),
    ]
