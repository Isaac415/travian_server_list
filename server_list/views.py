from django.shortcuts import render
from server_list.models import GameWorld
from django.shortcuts import redirect

# Create your views here.
def servers(request):
    gameworlds = GameWorld.objects.all()

    return render(request, "server_list/server_list.html", {"gameworlds": gameworlds})

def other(request):

    return redirect('servers')
