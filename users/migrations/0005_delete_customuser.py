# Generated by Django 3.2.5 on 2021-07-21 18:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20210721_1536'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]
