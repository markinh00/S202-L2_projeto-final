from game import Game
from player import Player
from team import Team
from valorant_CRUD import ValorantCRUD
from vct_americas import PlayOff


def verify_user_input(message: str, valid_inputs: list[str], use_VI=True):
    while True:
        if use_VI:
            message = message + "("
            for i in range(0, len(valid_inputs)):
                message = message + valid_inputs[i]
                if i < len(valid_inputs) - 1:
                    message = message + " | "
            message = message + "): "

        user_input = input(message)
        if user_input not in valid_inputs:
            print("Please type in a valid input!!")
        else:
            break

    return user_input


class ValorantCLI:
    def __init__(self, valorant_crud: ValorantCRUD):
        self.valorant_crud = valorant_crud
        self.playoff = PlayOff(self.valorant_crud)

    def start(self):
        while True:
            print("cp -> create player     | cg -> create game\n"
                  "rp -> read player stats | rg -> read game data\n"
                  "up -> update player     | gg -> get games played by a team\n"
                  "dp -> delete player     | ug -> update game\n"
                  "ct -> create team       | dg -> delete game\n"
                  "rt -> read team stats   | em -> emulate VCT Americas playoff\n"
                  "ut -> update team       | ex -> exit\n"
                  "dt -> delete team")
            valid_inputs = ["cp", "rp", "up", "dp", "ct", "rt", "ut", "dt", "cg", "rg", "gg", "ug", "dg", "em", "ex"]
            user_input = verify_user_input("Type in one of the options above: ", valid_inputs, False)

            if user_input == "cp": self.create_player()
            if user_input == "rp": self.read_player()
            if user_input == "up": self.update_player()
            if user_input == "dp": self.delete_player()
            if user_input == "ct": self.create_team()
            if user_input == "rt": self.read_team()
            if user_input == "ut": self.update_team()
            if user_input == "dt": self.delete_team()
            if user_input == "cg": self.create_game()
            if user_input == "rg": self.read_game()
            if user_input == "gg": self.get_games()
            if user_input == "ug": self.update_game()
            if user_input == "dg": self.delete_game()
            if user_input == "em": self.playoff.emulate()
            if user_input == "ex":
                print("Goodbye!!")
                break

    def create_player(self):
        while True:
            player_name = input("Player's name to be created: ")
            player_nationality = input("Player's nationality: ")
            new_player = Player(player_id=None, name=player_name, nationality=player_nationality)

            self.valorant_crud.create_player(new_player)

            verified_user_input = verify_user_input("Create another player? ", ["y", "n"])
            if verified_user_input == "n":
                break

    def read_player(self):
        while True:
            player_key = verify_user_input("Read player using id or name? ", ["id", "name"])
            player_value = input(f"Type in the player's {player_key}")

            result = self.valorant_crud.read_player({"key": player_key, "value": player_value})

            if result:
                print(f"name: {result['player_name']} | "
                      f"nationality: {result['nationality']} | "
                      f"id: {result['player_id']}")

            verified_user_input = verify_user_input("Get another player data? ", ["y", "n"])
            if verified_user_input == "n":
                break

    def update_player(self):
        while True:
            player_id = input("Player's id to updated: ")
            message = "which field do you whant to update? "
            player_key = verify_user_input(message, ["nationality", "name"])
            player_value = input(f"Type in the player's {player_key}")

            self.valorant_crud.update_player(player_id, {"key": player_key, "value": player_value})

            verified_user_input = verify_user_input("Update another player? ", ["y", "n"])
            if verified_user_input == "n":
                break

    def delete_player(self):
        while True:
            player_id = input("User's id to be deleted: ")

            self.valorant_crud.delete_player(player_id)

            verified_user_input = verify_user_input("Delete another player? : ", ["y", "n"])
            if verified_user_input == "n":
                break

    def create_team(self):
        while True:
            team_name = input("Team's name to be created: ")
            new_team = Team(team_id=None, name=team_name, list_of_players=[])

            self.valorant_crud.create_team(new_team)

            verified_user_input = verify_user_input("Create another team? ", ["y", "n"])
            if verified_user_input == "n":
                break

    def read_team(self):
        while True:
            team_name = input("Team's name to be read: ")

            team = self.valorant_crud.read_team({"key": "name", "value": team_name})
            if team:
                print(f"Team's name: {team['name']} | team's id: {team['team_id']}\n"
                      f"List of players: ")
                for player in team["players"]:
                    print(f"Player's name: {player['name']} | "
                          f"nationality: {player['nationality']} | "
                          f"id: {player['player_id']}")

            verified_user_input = verify_user_input("Read another team stats? ", ["y", "n"])
            if verified_user_input == "n":
                break

    def update_team(self):
        while True:
            message = "Add a player, remove a player or change team's name? "
            update_team = verify_user_input(message, ["a", "r", "c"])

            if update_team == "a":
                add_team_input = input("Team's name to add player: ")
                while True:
                    add_player_input = input(f"{add_team_input}'s new player name: ")

                    self.valorant_crud.add_player_to_team(add_player_input, add_team_input)

                    verified_user_input = verify_user_input(f"Add another player to {add_team_input}? ", ["y", "n"])
                    if verified_user_input == "n":
                        break

            if update_team == "r":
                team_name = input("Team's name to remove player: ")

                while True:
                    team = self.valorant_crud.read_team({"key": "name", "value": team_name})

                    print(f"List of {team_name}'s players: ")
                    for player in team["players"]:
                        print(f"Player's name: {player['name']} | "
                              f"nationality: {player['nationality']} | "
                              f"id: {player['player_id']}")

                    remove_player_input = input(f"Player's name to be removed from {team_name}: ")

                    self.valorant_crud.remove_player_from_team(remove_player_input, team_name)

                    verified_user_input = verify_user_input(f"Remove another player of {team_name}? ", ["y", "n"])
                    if verified_user_input == "n":
                        break

            if update_team == "c":
                team_name = input("Team's name to be changed: ")
                team_new_name = input(f"{team_name}'s new name: ")

                self.valorant_crud.update_team(team_name, {"key": "name", "value": team_new_name})

            verified_user_input = verify_user_input("Update another team? ", ["y", "n"])
            if verified_user_input == "n":
                break

    def delete_team(self):
        while True:
            team_name = input("Team's name to be deleted: ")

            self.valorant_crud.delete_team(team_name)

            verified_user_input = verify_user_input("Delete another team? ", ["y", "n"])
            if verified_user_input == "n":
                break

    def create_game(self):
        while True:
            team1_name = input("First team name to create a game: ")
            team2_name = input("Second team name to create a game: ")
            team2 = Team(team_id=None, name=team2_name, list_of_players=[])
            team1 = Team(team_id=None, name=team1_name, list_of_players=[])

            scoreboard = input("Game's scoreboard: ")
            game_map = input("Map played: ")
            game_winner = verify_user_input("Game winner ", [team1.get_name(), team2.get_name()])

            game = Game(game_id=None,
                        team1=team1,
                        team2=team2,
                        map_name=game_map,
                        scoreboard=scoreboard,
                        winner=team1 if game_winner == team1.get_name() else team2)

            self.valorant_crud.create_game(game)

            verified_user_input = verify_user_input("Create another game? ", ["y", "n"])
            if verified_user_input == "n":
                break

    def read_game(self):
        while True:
            game_id = input("Game id: ")

            result = self.valorant_crud.read_game({'key': 'game_id', 'value': game_id})
            if result:
                game = result['game']
                team1 = result['team1']
                team2 = result['team2']
                print(f"Game stats:"
                      f"scoreboard: {game['scoreboard']} | "
                      f"map: {game['map']} | "
                      f"winner: {game['winner']} | "
                      f"id: {game['game_id']}\n"
                      f"Team's that played the game: \n"
                      f"name: {team1['name']} | id: {team1['team_id']}\n"
                      f"name: {team2['name']} | id: {team2['team_id']}")

            verified_user_input = verify_user_input("Read another game? ", ["y", "n"])
            if verified_user_input == "n":
                break

    def get_games(self):
        while True:
            team_name = input("Team's name: ")
            results = self.valorant_crud.get_games_played(team_name)
            if results:
                for result in results:
                    game = result['game']
                    team1 = result['team1']
                    team2 = result['team2']
                    print(f"Game stats:"
                          f"scoreboard: {game['scoreboard']} | "
                          f"map: {game['map']} | "
                          f"winner: {game['winner']} | "
                          f"id: {game['game_id']}\n"
                          f"Team's that played the game: \n"
                          f"name: {team1['name']} | id: {team1['team_id']}\n"
                          f"name: {team2['name']} | id: {team2['team_id']}")

            verified_user_input = verify_user_input("Read another team games? ", ["y", "n"])
            if verified_user_input == "n":
                break

    def update_game(self):
        while True:
            game_id = input("Game's id to be updated: ")
            game_update_key = verify_user_input("which value to update? ", ["scoreboard", 'winner', 'map'])
            game_update_value = input(f"Game {game_id} new {game_update_key}: ")

            self.valorant_crud.update_game(game_id, {'key': game_update_key, 'value': game_update_value})

            verified_user_input = verify_user_input("Update another game? ", ["y", "n"])
            if verified_user_input == "n":
                break

    def delete_game(self):
        while True:
            game_id = input("Game's id to be deleted: ")

            self.valorant_crud.delete_game(game_id)

            verified_user_input = verify_user_input("Delete another game? ", ["y", "n"])
            if verified_user_input == "n":
                break
