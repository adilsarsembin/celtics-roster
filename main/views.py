from django.shortcuts import render
from django.http import HttpResponse

from . import models

# Create your views here.


def home(request):
    return render(request, 'main/home.html')


def players(request):
    all_players = models.Player.objects.all()

    context = {
        'all_players': all_players
    }
    return render(request, 'main/players.html', context)


def one_player(request, pk):
    slugs = list(models.Player.objects.values_list('slug'))
    slugs = [slug[0] for slug in slugs]

    if pk not in slugs:
        return HttpResponse('There is no player in Boston with such full name!')

    player_data = models.Player.objects.get(slug=pk)
    data = {
        'player_data': player_data
    }

    return render(request, 'main/one_player.html', data)


def schedule(request):
    return render(request, 'main/schedule.html')
