from team import Team
from bson.objectid import ObjectId


class Game:
    def __init__(self, game_id: [str, None], map_name: str, team1: Team, team2: Team, scoreboard: str, winner: Team):
        if not game_id:
            self.id = str(ObjectId())
        else:
            self.id = game_id
        self.map = map_name
        self.team1 = team1
        self.team2 = team2
        self.scoreboard = scoreboard
        self.winner = winner

    def get_id(self) -> str:
        return self.id

    def get_map(self) -> str:
        return self.map

    def set_map(self, new_map_name: str) -> None:
        self.map = new_map_name
        return None

    def get_teams(self) -> list[Team]:
        return [self.team1, self.team2]

    def get_scoreboard(self) -> str:
        return self.scoreboard

    def set_scoreboard(self, new_scoreboard) -> None:
        self.scoreboard = new_scoreboard
        return None

    def get_winner(self) -> Team:
        return self.winner

    def set_winner(self, new_winner: Team) -> None:
        self.winner = new_winner
        return None

    def show_teams(self) -> None:
        print(f"{self.team1} players: \n")
        self.team1.show_players()
        print(f"{self.team2} players: \n")
        self.team2.show_players()
        print(" ")
        return None

    def asDict(self):
        dictionary = self.__dict__
        dictionary["_team1"] = [child.__dict__ for child in dictionary["_team1"]]
        dictionary["_team2"] = [child.__dict__ for child in dictionary["_team2"]]
        dictionary["_winner"] = [child.__dict__ for child in dictionary["_winner"]]
        return dictionary
