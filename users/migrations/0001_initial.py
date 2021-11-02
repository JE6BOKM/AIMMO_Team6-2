# Generated by Django 3.2.9 on 2021-11-02 03:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=16)),
                ('email', models.CharField(max_length=128)),
                ('password', models.CharField(max_length=512)),
            ],
            options={
                'db_table': 'users',
            },
        ),
    ]