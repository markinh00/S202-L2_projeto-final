from database import Database
from player import Player
from team import Team
from bson.objectid import ObjectId


class Valorant:
    def __init__(self, database: Database):
        self.db = database
        self.collections = database.collections

    def create_player(self, player: Player) -> None:
        try:
            result = self.collections["players"].insert_one(player.asDict())
            player_id = str(result.inserted_id)
            print(f"Player {player.get_name()} created with id: {player_id}")
            return None
        except Exception as error:
            print(f"An error occurred while creating player: {error}")
            return None

    def read_player_name(self, player_name: str) -> [Player, None]:
        try:
            player = self.collections["players"].find_one({"_name": player_name})
            if player:
                print(f"Player found: {player}")
                return player
            else:
                print(f"No player found with name {player_name}")
                return None
        except Exception as error:
            print(f"An error occurred while reading player: {error}")
            return None

    def read_player_id(self, player_id: str) -> [Player, None]:
        try:
            player = self.collections["players"].find_one({"_id": ObjectId(player_id)})
            if player:
                print(f"Player found: {player}")
                return player
            else:
                print(f"No player found with id {player_id}")
                return None
        except Exception as error:
            print(f"An error occurred while reading player: {error}")
            return None

    def update_player(self, player_id: str, values: dict) -> None:
        try:
            result = self.collections["players"].update_one({"_id": ObjectId(player_id)}, {"$set": values})
            if result.modified_count:
                print(f"Player {player_id} updated with values: ", values)
            else:
                print(f"No player found with id {player_id}")
            return None
        except Exception as error:
            print(f"An error occurred while updating player: {error}")

    def delete_player(self, player_id: str) -> [int, None]:
        try:
            team = self.collections["teams"].find_one({"_list_of_players": ObjectId(player_id)})
            team_id = team["_id"]
            if not team_id:
                print("Could not find the team the player is part of")
                return None
            else:
                result = self.collections["teams"].update_one({"_id": ObjectId(team_id)}, {
                    "$pull": {
                        "_list_of_players": ObjectId(player_id)
                    }
                })
                if not result.modified_count:
                    print("Could not delete player out off the team")
                    return None
                else:
                    result = self.collections["players"].delete_one({"_id": ObjectId(player_id)})
                    if not result.deleted_count:
                        print(f"No player found with id {player_id}")
                        return None
                    else:
                        print(f"Player {player_id} deleted")
                        return result.deleted_count
        except Exception as error:
            print(f"An error occurred while deleting player: {error}")
            return None

    def create_team(self, team: Team) -> None:
        for player in team.get_players():
            result = self.read_player_id(player.get_id())
            if not result:
                print(f"The team must have all the players created first!!")
                return None

        try:
            team_dict = {
                "_id": team.get_id(),
                "_name": team.get_name(),
                "_list_of_players": []
            }

            for player in team.get_players():
                team_dict["_list_of_players"].append(player.get_id())

            result = self.collections["teams"].insert_one(team_dict)
            team_id = str(result.inserted_id)
            if result:
                print(f"Team {team.get_name()} created with id: {team_id}")
                return None
        except Exception as error:
            print(f"An error occurred while creating team: {error}")
            return None

    def read_team_by_name(self, team_name: str) -> [dict, None]:
        try:
            team = self.collections["teams"].find_one({"_name": team_name})
            if team:
                player_list = []
                found_players = self.collections["players"].find({"_id": {"$in": team["_list_of_players"]}})
                if found_players:
                    for doc in found_players:
                        player_list.append(doc)
                    team["_list_of_players"] = player_list
                    print(f"Team found: {team}")
                return team
            else:
                print(f"No team found with name {team_name}")
                return None
        except Exception as error:
            print(f"An error occurred while reading team: {error}")
            return None

    def update_team(self, team_id: str, values: dict) -> None:
        try:
            result = self.collections["teams"].update_one({"_id": ObjectId(team_id)}, {"$set": values})
            if result.modified_count:
                print(f"Team {team_id} updated with values: ", values)
            else:
                print(f"No team found with id {team_id}")
            return None
        except Exception as error:
            print(f"An error occurred while updating team: {error}")

