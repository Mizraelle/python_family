# Generated by Django 2.1 on 2019-05-30 15:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('video', '0002_auto_20190527_2101'),
    ]

    operations = [
        migrations.CreateModel(
            name='Coment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('likes', models.PositiveIntegerField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Комментарий',
                'verbose_name_plural': 'Комментарии',
                'db_table': 'Комментарии',
            },
        ),
        migrations.AddField(
            model_name='video',
            name='date_video',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='video',
            name='di_video',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='video',
            name='likes_video',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='coment',
            name='video',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='video.Video'),
        ),
    ]