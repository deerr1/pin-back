# Generated by Django 3.2 on 2021-12-19 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='avatar',
            field=models.FileField(blank=True, null=True, upload_to='avatars', verbose_name='Аватар'),
        ),
    ]
