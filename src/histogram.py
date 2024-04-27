import json


class Histogram:
    def __init__(self, filename="highscores.json"):
        self.filename = filename
        self.highscores = self.load_highscores()

    def load_highscores(self):
        try:
            with open(self.filename, "r") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def update_highscore(self, player):
        name_key = player.original_name
        player_data = self.highscores.get(name_key, {"name": player.name, "best_score": 0, "games_played": 0})
        player_data["best_score"] = max(player_data["best_score"], player.score)
        player_data["games_played"] += 1
        player_data["name"] = player.name
        self.highscores[name_key] = player_data
        self.save_highscores()

    def save_highscores(self):
        with open(self.filename, "w") as file:
            json.dump(self.highscores, file, indent=4)

    def display_highscores(self):
        for record in self.highscores.values():
            print(f"{record['name']} - Best Score: {record['best_score']}, Games Played: {record['games_played']}")
