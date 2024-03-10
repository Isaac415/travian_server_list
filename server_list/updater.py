import os, django, sys
sys.path.append('../travian_server_list/')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'travian_server_list.settings')
django.setup()

import requests, hashlib
from bs4 import BeautifulSoup
from server_list.models import GameWorld

URL = "https://blog.travian.com/gameworld-schedule/"

def get_table():
    response = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.find('table', {'id': 'tablepress-3'})

def version_hash(table):
    return hashlib.sha256(str(table).encode()).hexdigest()

def update_game_worlds(table):
    count = 0
    game_worlds_rows = table.find_all('tr')[1: ]
    for row in game_worlds_rows:
        lines = row.find_all("td")
        try:
            url = lines[0].a["href"]
            game_world_id = url.split('/')[3]
            search = GameWorld.objects.filter(id=game_world_id)
            if len(search) != 0:
                continue
        except:
            continue

        server = lines[0].text.strip()
        speed = lines[1].text.strip()
        game_mode = lines[2].text.strip()
        num_of_tribes = int(lines[3].text.strip())
        start_date = lines[4].text.strip()
        start_time = lines[5].text.strip()
        artifacts_spawn_date = lines[6].text.strip()
        building_plans_spawn_date = lines[7].text.strip()
        end_condition = lines[8].text.strip()

        new_game_world = GameWorld(id=game_world_id, 
                                   url=url,
                                   server=server,
                                   speed=speed,
                                   game_mode=game_mode,
                                   num_of_tribes=num_of_tribes,
                                   start_date=start_date,
                                   start_time=start_time,
                                   artifacts_spawn_date=artifacts_spawn_date,
                                   building_plans_spawn_date=building_plans_spawn_date,
                                   end_condition=end_condition
                                   )
        new_game_world.save()
        count += 1
    
    return count

def update():
    table = get_table()
    update_game_worlds(table)

if "__main__" == __name__:
    num_of_new_game_worlds = update()
    print("New Game Worlds Added: " + str(num_of_new_game_worlds))