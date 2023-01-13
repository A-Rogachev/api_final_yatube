# Generated by Django 3.2.16 on 2023-01-13 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20230113_1430'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Укажите название группы', max_length=200, verbose_name='Название группы')),
                ('slug', models.SlugField(help_text='Укажите slug для url-адреса группы', unique=True, verbose_name='Slug для url-адреса')),
                ('description', models.TextField(help_text='Добавьте описание группы', verbose_name='Описание группы')),
            ],
            options={
                'verbose_name': 'Группа',
                'verbose_name_plural': 'Группы',
            },
        ),
    ]