import json


class DB:
    def __init__(self):
        with open("db.json", "r") as f:
            
            self.database = json.load(f)
        