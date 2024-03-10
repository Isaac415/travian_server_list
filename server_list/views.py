from django.shortcuts import render
from server_list.models import GameWorld
from django.shortcuts import redirect
from server_list.updater import update
from django.conf import settings
import time

def time_difference(original_time):
    time_difference = int(time.time() - original_time)

    if time_difference < 60:
        formatted_time = f"{time_difference} seconds ago"
    else:
        minutes = time_difference // 60
        formatted_time = f"{minutes} minutes ago"
    
    return formatted_time

# Create your views here.
def servers(request):
    if time.time() - settings.SERVER_LIST_LAST_UPDATE > 60 * 5:
        update()
        settings.SERVER_LIST_LAST_UPDATE = time.time()

    gameworlds = GameWorld.objects.all()

    context = {"gameworlds": gameworlds,
               "last_update": time_difference(settings.SERVER_LIST_LAST_UPDATE)}
    return render(request, "server_list/server_list.html", context)

def other(request):

    return redirect('servers')
