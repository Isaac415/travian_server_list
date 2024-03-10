class GameWorld:
    def __init__(self, url, id, server_no, speed, win_cond, 
                 num_of_tribes, start_date, start_time, artifact_spawn_date,
                 building_plans_spawn_date, end_cond):
        self.url = url
        self.id = id
        self.server_no = server_no
        self.speed = speed
        self.win_cond = win_cond
        self.num_of_tribes = num_of_tribes
        self.start_date = start_date
        self.start_time = start_time
        self.artifact_spawn_date = artifact_spawn_date
        self.building_plans_spawn_date = building_plans_spawn_date
        self.end_cond = end_cond
    
    def info(self):
        print("URL: " + str(self.url))
        print("ID: " + str(self.id))
        print("Server No.: " + str(self.server_no))
        print("Speed: " + str(self.speed))
        print("Win Condition: " + str(self.win_cond))
        print("Number of Tribes: " + str(self.num_of_tribes))
        print("Start Date: " + str(self.start_date))
        print("Start Time: " + str(self.start_time))
        print("Artifact Spawn Date: " + str(self.artifact_spawn_date))
        print("Building Plans Spawn Date: " + str(self.building_plans_spawn_date))
        print("End Condition: " + str(self.end_cond))
        