from django.contrib import admin
from .models import Event,SuccessStory

admin.site.register(Event)

@admin.register(SuccessStory)
class SuccessStoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image')  # Колонки в списке
    search_fields = ('title', 'description')  # Поиск по этим полям
    list_filter = ('title',)  # Фильтрация по этим полям
