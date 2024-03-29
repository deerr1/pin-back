# Generated by Django 3.2 on 2021-12-20 02:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название доски')),
                ('access', models.IntegerField(blank=True, choices=[(0, 'Открытая'), (1, 'Закрытая')], default=0, verbose_name='Право')),
            ],
        ),
        migrations.CreateModel(
            name='BoardPin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pins.board', verbose_name='Доска')),
            ],
            options={
                'verbose_name': 'Связь пинов с доской',
                'verbose_name_plural': 'Связь пинов с доской',
            },
        ),
        migrations.CreateModel(
            name='PinCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_category', models.CharField(max_length=50, verbose_name='Название категории')),
            ],
            options={
                'verbose_name': 'Категории пинов',
                'verbose_name_plural': 'Категории пинов',
            },
        ),
        migrations.CreateModel(
            name='UserRightBoard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pins.board')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Права пользователя на доску',
                'verbose_name_plural': 'Права пользователя на доску',
            },
        ),
        migrations.CreateModel(
            name='Pin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='Название пина')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Описание')),
                ('image', models.FileField(upload_to='images', verbose_name='Изображение')),
                ('upload_date', models.DateTimeField(verbose_name='Дата загрузки пина')),
                ('board', models.ManyToManyField(through='pins.BoardPin', to='pins.Board')),
                ('category', models.ManyToManyField(to='pins.PinCategory', verbose_name='Категория')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Пины',
                'verbose_name_plural': 'Пины',
            },
        ),
        migrations.AddField(
            model_name='boardpin',
            name='pin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pins.pin', verbose_name='Картинка'),
        ),
        migrations.AddField(
            model_name='board',
            name='user_righs_board',
            field=models.ManyToManyField(through='pins.UserRightBoard', to=settings.AUTH_USER_MODEL),
        ),
    ]
