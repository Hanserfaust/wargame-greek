from django.contrib import admin

# from markdownx.admin import MarkdownxModelAdmin

from wgg.models import Conflict, BoardGame, GameToConflict


class GameToConflictInline(admin.TabularInline):
    model = GameToConflict


class BoardGameOptions(admin.ModelAdmin):
    list_display = ['name', 'yearpublished', 'ratings_usersrated', 'ratings_average', 'ratings_averageweight']

    list_per_page = 200

    inlines = [
        GameToConflictInline,
    ]


admin.site.register(Conflict)
admin.site.register(BoardGame, BoardGameOptions)
admin.site.register(GameToConflict)
