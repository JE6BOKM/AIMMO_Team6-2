# Generated by Django 3.2.9 on 2021-11-02 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='counting',
            field=models.IntegerField(default=0),
        ),
    ]
