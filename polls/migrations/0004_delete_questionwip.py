# Generated by Django 4.1.5 on 2023-02-12 01:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_remove_questionwip_pub_date_questionwip_num_options'),
    ]

    operations = [
        migrations.DeleteModel(
            name='QuestionWIP',
        ),
    ]
