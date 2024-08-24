from django.db import models
from django.core.exceptions import ValidationError
class Scope(models.Model):
    name = models.CharField(max_length=256,verbose_name='Название раздела')

    class Meta:
        verbose_name = 'Раздел'
        verbose_name_plural = 'Разделы'
    def __str__(self):
        return self.name

class Article(models.Model):
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    scopes = models.ManyToManyField(Scope, through='ArticleScope', verbose_name='Разделы')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'

    def __str__(self):
        return self.title

    def get_scopes(self):
        return self.article_scopes.select_related('tag')

    def clean(self):
        main_scopes = self.article_scopes.filter(is_main=True)
        if main_scopes.count() > 1:
            raise ValidationError('У статьи может быть только один основной раздел.')

class ArticleScope(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='article_scopes')
    tag = models.ForeignKey(Scope, on_delete=models.CASCADE)
    is_main = models.BooleanField(default=False, verbose_name='Основной раздел')

    class Meta:
        unique_together = ('article', 'tag')
        verbose_name = 'Связь статьи с разделом'
        verbose_name_plural = 'Связи статьи с разделами'

    def __str__(self):
        return f'{self.article.title} - {self.tag.name} ({"Основной" if self.is_main else "Второстепенный"})'

    def clean(self):
        if self.is_main and self.article.article_scopes.filter(is_main=True).exclude(id=self.id).exists():
            raise ValidationError("У статьи может быть только один основной раздел.")