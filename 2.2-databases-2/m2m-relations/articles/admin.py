from django.contrib import admin
from .models import Article, Scope, ArticleScope

class ArticleScopeInline(admin.TabularInline):
    model = ArticleScope
    extra = 1

class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleScopeInline]

    def save_related(self, request, form, formsets, change):
        super().save_related(request, form, formsets, change)
        obj = form.instance
        main_scopes = obj.article_scopes.filter(is_main=True)
        if main_scopes.count() != 1:
            raise ValueError('У статьи должен быть один и только один основной разделю')

admin.site.register(Scope)
admin.site.register(Article, ArticleAdmin)
