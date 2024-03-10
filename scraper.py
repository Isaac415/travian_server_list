import requests
from bs4 import BeautifulSoup
import hashlib
from gameworld import GameWorld

URL = "https://blog.travian.com/gameworld-schedule/"

def get_table():
    response = requests.get(URL, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.find('table', {'id': 'tablepress-3'})

def version_hash(table):
    return hashlib.sha256(str(table).encode()).hexdigest()

def get_game_world_rows(table):
    return table.find_all('tr')[1: ]

def tokenize_game_worlds(game_worlds_rows):
    game_words = list() # list of GameWorld objects
    for row in game_worlds_rows:
        lines = row.find_all("td")
        try:
            url = lines[0].a["href"]
            game_world_id = url.split('/')[-2]
        except:
            url, game_world_id = None, None

        region = lines[0].text.strip().split()[:-1]
        server = lines[0].text.strip().split()[-1:]
        speed = lines[1].text.strip()
        win_condition = lines[2].text.strip()
        num_of_tribes = lines[3].text.strip()
        start_date = lines[4].text.strip()
        start_time = lines[5].text.strip()
        artifacts_spawn_date = lines[6].text.strip()
        building_plans_spwan_date = lines[7].text.strip()
        end_condition = lines[8].text.strip()
        '''
        game_words.append(GameWorld(url, server_id, server_number, speed,
                                    win_condition, num_of_tribes,
                                    start_date, start_time, artifacts_spawn_date,
                                    building_plans_spwan_date, end_condition))
        '''
        print("Region: " + str(region))
        print("Server: " + str(server))
        print()
    return game_words


table = get_table()
game_worlds_rows = get_game_world_rows(table)
tokenize_game_worlds(game_worlds_rows)