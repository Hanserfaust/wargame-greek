from django.http import HttpResponse, HttpResponseRedirect, Http404, HttpResponseForbidden, HttpResponseNotAllowed
from django.shortcuts import render

from wgg.models import *


def wgg_home(request):
    # Load stats etc.
    return render(request, 'wgg_home.html', {})


def wgg_games(request):

    return render(request, 'wgg_games.html', {
        'games': BoardGame.objects.filter(ratings_average__gt=6.9).filter(ratings_usersrated__gt=50).order_by('-ratings_average')
    })


def wgg_conflicts(request):

    return render(request, 'wgg_conflicts.html', {
        'conflicts': Conflict.objects.all(),
    })


