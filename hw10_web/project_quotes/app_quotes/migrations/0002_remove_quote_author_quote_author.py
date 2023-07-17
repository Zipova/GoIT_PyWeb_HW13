# Generated by Django 4.2.1 on 2023-07-17 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_quotes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quote',
            name='author',
        ),
        migrations.AddField(
            model_name='quote',
            name='author',
            field=models.ManyToManyField(to='app_quotes.author'),
        ),
    ]