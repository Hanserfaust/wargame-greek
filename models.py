from django.db import models


class Conflict(models.Model):
    title = models.CharField(max_length=128)

    part_of = models.ForeignKey("Conflict", on_delete=models.CASCADE, blank=True, null=True)
    aliases = models.TextField(blank=True)

    start_date = models.DateField(blank=True, null=True)
    end_date = models.DateField(blank=True, null=True)

    # English wikipedia stuff
    en_wiki_url = models.URLField(blank=True)
    wiki_api_data_cache = models.TextField(blank=True)

    created = models.DateTimeField(auto_created=True, auto_now_add=True)

    def __str__(self):
        return u'%s (%s - %s)' % (self.title, self.start_date.year, self.end_date.year)

class BoardGame(models.Model):

    bgg_id = models.IntegerField(primary_key=True)

    name = models.CharField(max_length=256)

    yearpublished = models.IntegerField(blank=True)
    description = models.TextField()
    image = models.URLField(null=True)
    thumbnail = models.URLField(null=True)

    playingtime = models.IntegerField()

    designers = models.CharField(max_length=512, blank=True)
    publishers = models.CharField(max_length=512, blank=True)

    mechanics = models.CharField(max_length=512, blank=True)
    categories = models.CharField(max_length=512, blank=True)

    minplayers = models.IntegerField()
    maxplayers = models.IntegerField()

    ratings_usersrated = models.IntegerField()
    ratings_average = models.FloatField()
    ratings_averageweight = models.FloatField()

    bgg_json = models.TextField(blank=True)

    def update_from_bgg(self):
        pass

    def __str__(self):
        return self.name


class GameToConflict(models.Model):
    # This is the many-to-many helper table
    # since a game cover several unrelated conflicts, battles etc.
    # we need to add one of these for each game and conflict

    game = models.ForeignKey(BoardGame, on_delete=models.PROTECT)
    conflict = models.ForeignKey(Conflict, on_delete=models.PROTECT)

    coverage = models.IntegerField(default=100)

    def __str__(self):
        return '%s <-> %s' % (self.game.name, self.conflict.title)
