from player import Player
from bson.objectid import ObjectId


class Team:
    def __init__(self, team_id: [str, None], name: str, list_of_players: list[Player]):
        if not team_id:
            self._id = ObjectId()
        else:
            self._id = team_id
        self._name = name
        self._list_of_players = list_of_players

    def get_id(self) -> str:
        return self._id

    def get_name(self) -> str:
        return self._name

    def set_name(self, new_name: str) -> None:
        self._name = new_name
        return None

    def add_player(self, new_player: Player) -> None:
        for player in self._list_of_players:
            if player.get_id() == new_player.get_id():
                print("Player already created!!")
                return None

        self._list_of_players.append(new_player)
        print("Player created successfully!!")
        return None

    def get_player(self, player_id: [str, None], player_name: [str, None]) -> [Player, None]:
        if player_id is not None:
            list_filter = player_id
        else:
            list_filter = player_name

        for player in self._list_of_players:
            if player.get_id() == list_filter or player.get_name() == list_filter:
                return player

        print("Player not found!!")
        return None

    def get_players(self) -> [list[Player], None]:
        if len(self._list_of_players) == 0:
            print(f"The team {self._name} has no players!!")
            return None

        return self._list_of_players

    def show_players(self) -> None:
        if len(self._list_of_players) == 0:
            print(f"The team {self._name} has no players!!")
            return None

        for player in self._list_of_players:
            player.show_stats()
        return None

    def delete_player(self, player_id: str) -> None:
        if len(self._list_of_players) == 0:
            print("No player found in the team!!")
            return None

        for player in self._list_of_players:
            if player.get_id() == player_id:
                self._list_of_players.remove(player)
                print("player removed successfully!!")
                return None

        print("Player not found!!")
        return None

    def asDict(self):
        dictionary = self.__dict__
        dictionary["_list_of_players"] = [child.__dict__ for child in dictionary["_list_of_players"]]
        return dictionary
