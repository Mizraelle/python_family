from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
from django.utils.safestring import mark_safe


class Video(models.Model):
    class Meta:
        verbose_name = "Видео"
        verbose_name_plural = "Много видео"

    name_video = models.CharField(max_length=100, null=True, blank=True, verbose_name='видео ччч', help_text='просто текст')
    url_video = models.URLField(null=True)
    di_video = models.TextField(null=True)
    date_video = models.DateTimeField(auto_now_add=True, null=True)
    likes_video = models.PositiveIntegerField(default=0)
    slug = models.SlugField(null=True, unique=True)


    @property
    def videoplay(self):
        return mark_safe('<iframe width="100" height="50" src="' + self.url_video + '" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>')

    def __str__(self):
        return self.name_video


class Comment(models.Model):
    class Meta:
        db_table = "Комментарии"
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    text = models.TextField()
    likes = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)


# Create your models here.


