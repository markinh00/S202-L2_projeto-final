from team import Team
from bson.objectid import ObjectId


class Match:
    def __init__(self, match_id: [str, None], team1: Team, team2: Team, result: str, winner: Team):
        if not match_id:
            self._id = ObjectId()
        else:
            self._id = match_id
        self._team1 = team1
        self._team2 = team2
        self._result = result
        self._winner = winner

    def get_teams(self) -> list[Team]:
        return [self._team1, self._team2]

    def get_result(self) -> str:
        return self._result

    def set_result(self, new_result) -> None:
        self._result = new_result
        return None

    def get_winner(self) -> Team:
        return self._winner

    def set_winner(self, new_winner: Team) -> None:
        self._winner = new_winner
        return None

    def show_teams(self) -> None:
        print(f"{self._team1} players: \n")
        self._team1.show_players()
        print(f"{self._team2} players: \n")
        self._team2.show_players()
        print(" ")
        return None

    def asDict(self):
        dictionary = self.__dict__
        dictionary["_team1"] = [child.__dict__ for child in dictionary["_team1"]]
        dictionary["_team2"] = [child.__dict__ for child in dictionary["_team2"]]
        dictionary["_winner"] = [child.__dict__ for child in dictionary["_winner"]]
        return dictionary
