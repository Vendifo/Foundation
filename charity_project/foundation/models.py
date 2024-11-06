from django.db import models
from django.utils.text import slugify
from django.utils import timezone

class Event(models.Model):
    title = models.CharField(max_length=255)
    full_description = models.TextField(default="Описание отсутствует")  # Поле с дефолтным значением
    image = models.ImageField(upload_to='events/')
    date = models.DateField(default=timezone.now)  # Добавить default
    location = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        # Генерация slug на основе названия события
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title




class SuccessStory(models.Model):
    title = models.CharField(max_length=200)  # Название истории
    description = models.TextField()  # Краткое описание истории
    image = models.ImageField(upload_to='success_stories/', blank=True, null=True)  # Изображение (необязательно)
    
    def __str__(self):
        return self.title
