from database import Database
from game import Game
from player import Player
from team import Team
import pandas as pd


class ValorantCRUD:
    def __init__(self, database: Database):
        self.db = database

    def create_player(self, player: Player) -> None:
        try:
            result = self.read_player({'key': "name", 'value': player.get_name()})
            if result:
                print(f"Player with name {player.get_name()} already exists")
                return None
            else:
                query = "CREATE (:Player {player_id: $player_id, name: $name, nationality: $nationality})"
                parameters = {
                    "player_id": player.get_id(),
                    "name": player.get_name(),
                    "nationality": player.get_nationality()
                }
                self.db.execute_query(query, parameters)
                print(f"Player {player.get_name()} created successfully")
                return None
        except Exception as error:
            print(f"An error occurred while creating player {player.get_name()}:", error)

    def read_player(self, values: dict) -> [dict, None]:
        try:
            query = f"MATCH(p:Player) " \
                    f"WHERE p.{values['key']} = $value " \
                    f"RETURN p AS player"
            parameters = {"value": values['value']}
            result = self.db.execute_query(query, parameters)

            if not result:
                print(f"No player found with {values['key']}: {values['value']}")
                return None
            else:
                return result[0]["player"]
        except Exception as error:
            print(f"An error occurred while reading player with {values['key']} {values['value']}:", error)

    def get_players_without_team(self) -> [list, None]:
        try:
            query = "MATCH(p:Player), (t:Team)"\
                    "WHERE NOT(EXISTS((p)-[:PLAYS_FOR]->(t)))"\
                    "RETURN p AS player"
            parameters = {}
            result = self.db.execute_query(query, parameters)
            if not result:
                print("No player without a team found")
                return None
            else:
                players = []
                for item in result:
                    players.append(item['player'])

                df = pd.DataFrame(players)
                df.drop_duplicates(subset=['name'], keep='last', inplace=True)
                players = df.to_dict("records")
                # print(type(players))
                return players
        except Exception as error:
            print("An error occurred while getting all player without team:", error)

    def update_player(self, player_id: str, values: dict) -> None:
        try:
            query = "MATCH(p:Player)" \
                    f"WHERE p.player_id = '{player_id}'" \
                    f"SET p.{values['key']} = $new_value"
            parameters = {"new_value": values['value']}

            self.db.execute_query(query, parameters)
            print(f"Player {player_id} updated successfully")
        except Exception as error:
            print(f"An error occurred while updating player {player_id}:", error)

    def delete_player(self, player_id: str) -> None:
        try:
            query = "MATCH(p:Player) " \
                    "WHERE p.player_id = $player_id " \
                    "DETACH DELETE p"
            parameters = {"player_id": player_id}

            self.db.execute_query(query, parameters)
            print(f"Player {player_id} deleted successfully")
        except Exception as error:
            print(f"An error occurred while deleting player {player_id}:", error)

    def team_exists(self, values: dict) -> bool:
        try:
            query = f"MATCH (t:Team) " \
                    f"WHERE t.{values['key']} = $value " \
                    f"RETURN t"
            parameters = {"value": values['value']}
            result = self.db.execute_query(query, parameters)
            if result:
                return True
            else:
                return False
        except Exception as error:
            print(f"An error occured while verifing if team {values['value']} exists:", error)

    def create_team(self, team: Team) -> None:
        try:
            result = self.team_exists({'key': 'name', 'value': team.get_name()})
            if result:
                print(f"Team with name {team.get_name()} already exists")
                return None
            else:
                query = "CREATE(t:Team{team_id: $team_id, name: $name})"
                parameters = {"team_id": team.get_id(), "name": team.get_name()}

                self.db.execute_query(query, parameters)
                print(f"Team {team.get_name()} created successfully")
        except Exception as error:
            print("An error occurred while creating team:", error)

    def read_team(self, values: dict) -> [dict, None]:
        try:
            query = f"MATCH (p:Player)-[:PLAYS_FOR]->(t:Team) " \
                    f"WHERE t.{values['key']} = $value " \
                    f"RETURN t AS team, p AS player"
            parameters = {"value": values['value']}
            result = self.db.execute_query(query, parameters)

            if not result:
                print(f"No team found with {values['key']}: {values['value']}")
                return None
            else:
                team = {"players": []}

                for item in result:
                    if "player" in item.keys():
                        team["players"].append(item['player'])
                    if "team" in item.keys():
                        for key in item["team"].keys():
                            team[key] = item["team"][key]
                return team
        except Exception as error:
            print(f"An error occurred while reading team with {values['key']} {values['value']}:", error)

    def player_has_team(self, player_id: str):
        try:
            query = f"MATCH(p:Player)-[:PLAYS_FOR]->(t:Team) " \
                    f"WHERE p.player_id = $player_id " \
                    f"RETURN p"
            parameters = {"player_id": player_id}
            result = self.db.execute_query(query, parameters)
            if result:
                return result
            else:
                return None
        except Exception as error:
            print("An error occurred while verifing if player has a team:", error)

    def add_player_to_team(self, player_name: str, team_name: str) -> None:
        try:
            if self.player_has_team(player_name):
                print(f"Player {player_name} already has a team")
                return None

            query = "MATCH(p:Player{name: $player_name}),(t:Team{name: $team_name})" \
                    "CREATE (p)-[:PLAYS_FOR]->(t)"
            parameters = {"player_name": player_name, "team_name": team_name}

            self.db.execute_query(query, parameters)
            print(f"Player {player_name} added to team {team_name} successfully")
        except Exception as error:
            print("An error occurred while adding player to team:", error)

    def remove_player_from_team(self, player_name: str, team_name: str) -> None:
        try:
            query = "MATCH (p:Player{name: $player_name})-[r:PLAYS_FOR]->(t:Team{name: $team_name}) " \
                    "DELETE r"
            parameters = {
                "player_name": player_name,
                "team_name": team_name
            }

            self.db.execute_query(query, parameters)
            print("Player removed from team successfully")
        except Exception as error:
            print("An error occurred while removing player from team:", error)

    def update_team(self, team_name: str, values: dict) -> None:
        try:
            query = "MATCH(t:Team) " \
                    "WHERE t.name = $team_name " \
                    f"SET t.{values['key']} = $new_value"
            parameters = {"team_name": team_name, "new_value": values["value"]}

            self.db.execute_query(query, parameters)
            print(f"Team {team_name} updated successfully")
        except Exception as error:
            print("An error occurred while updating team:", error)

    def delete_team(self, team_name: str) -> None:
        try:
            query = "MATCH(t:Team) " \
                    "WHERE t.name = $team_name " \
                    "DETACH DELETE t"
            parameters = {"team_name": team_name}

            self.db.execute_query(query, parameters)
            print(f"Team {team_name} deleted successfully")
        except Exception as error:
            print(f"An error occurred while deleting team {team_name}:", error)

    def create_game(self, game: Game) -> None:
        try:
            for team in game.get_teams():
                if not self.read_team({"key": "name", "value": team.get_name()}):
                    print(f"Could not create Game, team {team.get_name()} not created")
                    return None

            query = "MATCH(t1:Team{name: $team1_name}), (t2:Team{name: $team2_name})" \
                    "CREATE(g:Game{" \
                    "game_id: $game_id, " \
                    "map: $map, " \
                    "scoreboard: $scoreboard, " \
                    "winner: $winner}), " \
                    "(t1)-[:PLAYED]->(g), " \
                    "(t2)-[:PLAYED]->(g)"
            parameters = {
                "team1_name": game.get_teams()[0].get_name(),
                "team2_name": game.get_teams()[1].get_name(),
                "game_id": game.get_id(),
                "map": game.get_map(),
                "scoreboard": game.get_scoreboard(),
                "winner": game.get_winner().get_name()
            }
            self.db.execute_query(query, parameters)
            print(f"Game {game.get_teams()[0].get_name()} x {game.get_teams()[1].get_name()} created successfully")
        except Exception as error:
            print(f"An error occurred while creating game {game.get_id()}:", error)

    def read_game(self, values: dict) -> [dict, None]:
        try:
            query = f"MATCH(t1:Team)-[r:PLAYED]->(g:Game)<-[:PLAYED]-(t2:Team) " \
                    f"WHERE g.{values['key']} = $value " \
                    f"RETURN g AS game, t1 AS team1, t2 AS team2"
            parameters = {"value": values['value']}
            result = self.db.execute_query(query, parameters)
            if not result:
                print(f"No game found with {values['key']}: {values['value']}")
                return None
            else:
                return result[0]
        except Exception as error:
            print(f"An error occurred while reading game with {values['key']} { values['value']}:", error)

    def get_games_played(self, team_name: str) -> [dict, None]:
        try:
            query = f"MATCH(t1:Team)-[:PLAYED]->(g:Game)<-[:PLAYED]-(t2:Team)" \
                    f"WHERE t1.name = $team_name " \
                    f"RETURN g AS game, t1 AS team1, t2 AS team2"
            parameters = {"team_name": team_name}

            result = self.db.execute_query(query, parameters)
            return result
        except Exception as error:
            print(f"An error occurred while getting games played by {team_name}:", error)

    def update_game(self, game_id: str, values: dict) -> None:
        try:
            query = "MATCH (g:Game) " \
                    "WHERE g.game_id = $game_id " \
                    f"SET g.{values['key']} = $value"
            parameters = {
                "game_id": game_id,
                "value": values['value']
            }

            self.db.execute_query(query, parameters)
            print(f"Game {game_id} updated successfully")
        except Exception as error:
            print(f"An error occurred while updating game {game_id}:", error)

    def delete_game(self, game_id: str) -> None:
        try:
            query = "MATCH(g:Game) " \
                    "WHERE g.game_id = $game_id " \
                    "DETACH DELETE g"
            parameters = {"game_id": game_id}

            self.db.execute_query(query, parameters)
            print(f"Game {game_id} deleted successfully")
        except Exception as error:
            print(f"An error occurred while deleting game {game_id}:", error)
