# Generated by Django 2.1 on 2019-05-27 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='video',
            options={'verbose_name': 'Видео', 'verbose_name_plural': 'Много видео'},
        ),
        migrations.AddField(
            model_name='video',
            name='url_video',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='name_video',
            field=models.CharField(blank=True, default='hello', help_text='просто текст', max_length=100, null=True, verbose_name='видео ччч'),
        ),
    ]
