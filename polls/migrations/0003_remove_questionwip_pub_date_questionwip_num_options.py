# Generated by Django 4.1.5 on 2023-02-10 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_questionwip'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questionwip',
            name='pub_date',
        ),
        migrations.AddField(
            model_name='questionwip',
            name='num_options',
            field=models.IntegerField(default=2),
        ),
    ]
