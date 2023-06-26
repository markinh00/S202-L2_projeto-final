from game import Game
from player import Player
from team import Team
from valorant_CRUD import ValorantCRUD


class PlayOff:
    def __init__(self, valorant_crud: ValorantCRUD):
        self.valorant_crud = valorant_crud

    def emulate(self):
        loud_players = [Player(player_id=None, name="aspas", nationality="Brazil"),
                        Player(player_id=None, name="saadhak", nationality="Argentina"),
                        Player(player_id=None, name="tuyz", nationality="Brazil"),
                        Player(player_id=None, name="less", nationality="Brazil"),
                        Player(player_id=None, name="cauanzin", nationality="Brazil")]
        loud = Team(team_id=None, name="Loud", list_of_players=loud_players)

        for player in loud_players:
            self.valorant_crud.create_player(player)
        self.valorant_crud.create_team(loud)
        for player in loud_players:
            self.valorant_crud.add_player_to_team(player.get_name(), loud.get_name())

        nrg_players = [Player(player_id=None, name="FINESSE", nationality="Canada"),
                       Player(player_id=None, name="s0m", nationality="USA"),
                       Player(player_id=None, name="crashies", nationality="USA"),
                       Player(player_id=None, name="ardiis", nationality="Latvia"),
                       Player(player_id=None, name="Victor", nationality="USA")]
        nrg = Team(team_id=None, name="NRG Esports", list_of_players=nrg_players)

        for player in nrg_players:
            self.valorant_crud.create_player(player)
        self.valorant_crud.create_team(nrg)
        for player in nrg_players:
            self.valorant_crud.add_player_to_team(player.get_name(), nrg.get_name())

        eg_players = [Player(player_id=None, name="Boostio", nationality="USA"),
                      Player(player_id=None, name="C0M", nationality="USA"),
                      Player(player_id=None, name="jawgemo", nationality="Cambodia"),
                      Player(player_id=None, name="Ethan", nationality="USA"),
                      Player(player_id=None, name="Demon1", nationality="USA")]
        eg = Team(team_id=None, name="Evil Geniuses", list_of_players=eg_players)

        for player in eg_players:
            self.valorant_crud.create_player(player)
        self.valorant_crud.create_team(eg)
        for player in eg_players:
            self.valorant_crud.add_player_to_team(player.get_name(), eg.get_name())

        c9_players = [Player(player_id=None, name="Zellsis", nationality="USA"),
                      Player(player_id=None, name="Xeppaa", nationality="USA"),
                      Player(player_id=None, name="leaf", nationality="USA"),
                      Player(player_id=None, name="jakee", nationality="USA"),
                      Player(player_id=None, name="runi", nationality="USA")]
        c9 = Team(team_id=None, name="Cloud9", list_of_players=c9_players)

        for player in c9_players:
            self.valorant_crud.create_player(player)
        self.valorant_crud.create_team(c9)
        for player in c9_players:
            self.valorant_crud.add_player_to_team(player.get_name(), c9.get_name())

        lev_players = [Player(player_id=None, name="nzr", nationality="Argentina"),
                       Player(player_id=None, name="Tacolilla", nationality="Chile"),
                       Player(player_id=None, name="Mazino", nationality="Chile"),
                       Player(player_id=None, name="kiNgg", nationality="Chile"),
                       Player(player_id=None, name="shyy", nationality="Chile")]
        lev = Team(team_id=None, name="Leviatán", list_of_players=lev_players)

        for player in lev_players:
            self.valorant_crud.create_player(player)
        self.valorant_crud.create_team(lev)
        for player in lev_players:
            self.valorant_crud.add_player_to_team(player.get_name(), lev.get_name())

        furia_players = [Player(player_id=None, name="mwzera", nationality="Brazil"),
                         Player(player_id=None, name="Quick", nationality="Brazil"),
                         Player(player_id=None, name="Khalil", nationality="Brazil"),
                         Player(player_id=None, name="Mazin", nationality="Brazil"),
                         Player(player_id=None, name="dgzin", nationality="Brazil")]
        furia = Team(team_id=None, name="FURIA", list_of_players=furia_players)

        for player in furia_players:
            self.valorant_crud.create_player(player)
        self.valorant_crud.create_team(furia)
        for player in furia_players:
            self.valorant_crud.add_player_to_team(player.get_name(), furia.get_name())

        lev_furia1 = Game(None, "Ascent", team1=lev, team2=furia, scoreboard="5x13", winner=furia)
        lev_furia2 = Game(None, "Pearl", team1=lev, team2=furia, scoreboard="20x18", winner=lev)
        lev_furia3 = Game(None, "Ascent", team1=lev, team2=furia, scoreboard="6x13", winner=furia)

        self.valorant_crud.create_game(lev_furia1)
        self.valorant_crud.create_game(lev_furia2)
        self.valorant_crud.create_game(lev_furia3)

        nrg_eg1 = Game(None, "Haven", team1=nrg, team2=eg, scoreboard="13x11", winner=nrg)
        nrg_eg2 = Game(None, "Split", team1=nrg, team2=eg, scoreboard="13x15", winner=eg)
        nrg_eg3 = Game(None, "Ascent", team1=nrg, team2=eg, scoreboard="7x13", winner=eg)

        self.valorant_crud.create_game(nrg_eg1)
        self.valorant_crud.create_game(nrg_eg2)
        self.valorant_crud.create_game(nrg_eg3)

        loud_furia1 = Game(None, "Haven", team1=loud, team2=furia, scoreboard="13x4", winner=loud)
        loud_furia2 = Game(None, "Ascent", team1=loud, team2=furia, scoreboard="13x5", winner=loud)

        self.valorant_crud.create_game(loud_furia1)
        self.valorant_crud.create_game(loud_furia2)

        c9_eg1 = Game(None, "Fracture", team1=c9, team2=eg, scoreboard="5x13", winner=eg)
        c9_eg2 = Game(None, "Bind", team1=c9, team2=eg, scoreboard="2x13", winner=eg)

        self.valorant_crud.create_game(c9_eg1)
        self.valorant_crud.create_game(c9_eg2)

        c9_lev1 = Game(None, "Haven", team1=c9, team2=lev, scoreboard="13x8", winner=c9)
        c9_lev2 = Game(None, "Lotus", team1=c9, team2=lev, scoreboard="10x13", winner=lev)
        c9_lev3 = Game(None, "Ascent", team1=c9, team2=lev, scoreboard="13x4", winner=c9)

        self.valorant_crud.create_game(c9_lev1)
        self.valorant_crud.create_game(c9_lev2)
        self.valorant_crud.create_game(c9_lev3)

        furia_nrg1 = Game(None, "Bind", team1=furia, team2=nrg, scoreboard="9x13", winner=nrg)
        furia_nrg2 = Game(None, "Haven", team1=furia, team2=nrg, scoreboard="10x13", winner=nrg)

        self.valorant_crud.create_game(furia_nrg1)
        self.valorant_crud.create_game(furia_nrg2)

        loud_eg1 = Game(None, "Fracture", team1=loud, team2=eg, scoreboard="13x9", winner=loud)
        loud_eg2 = Game(None, "Ascent", team1=loud, team2=eg, scoreboard="11x13", winner=eg)
        loud_eg3 = Game(None, "Bind", team1=loud, team2=eg, scoreboard="13x3", winner=loud)

        self.valorant_crud.create_game(loud_eg1)
        self.valorant_crud.create_game(loud_eg2)
        self.valorant_crud.create_game(loud_eg3)

        c9_nrg1 = Game(None, "Pearl", team1=c9, team2=nrg, scoreboard="13x10", winner=c9)
        c9_nrg2 = Game(None, "Lotus", team1=c9, team2=nrg, scoreboard="9x13", winner=nrg)
        c9_nrg3 = Game(None, "Haven", team1=c9, team2=nrg, scoreboard="12x14", winner=nrg)

        self.valorant_crud.create_game(c9_nrg1)
        self.valorant_crud.create_game(c9_nrg2)
        self.valorant_crud.create_game(c9_nrg3)

        eg_nrg1 = Game(None, "Haven", team1=eg, team2=nrg, scoreboard="13x11", winner=eg)
        eg_nrg2 = Game(None, "Ascent", team1=eg, team2=nrg, scoreboard="8x13", winner=nrg)
        eg_nrg3 = Game(None, "Lotus", team1=eg, team2=nrg, scoreboard="10x13", winner=nrg)
        eg_nrg4 = Game(None, "Split", team1=eg, team2=nrg, scoreboard="4x13", winner=nrg)

        self.valorant_crud.create_game(eg_nrg1)
        self.valorant_crud.create_game(eg_nrg2)
        self.valorant_crud.create_game(eg_nrg3)
        self.valorant_crud.create_game(eg_nrg4)

        loud_nrg1 = Game(None, "Ascent", team1=loud, team2=nrg, scoreboard="13x9", winner=loud)
        loud_nrg2 = Game(None, "Bind", team1=loud, team2=nrg, scoreboard="13x11", winner=loud)
        loud_nrg3 = Game(None, "Fracture", team1=loud, team2=nrg, scoreboard="13x11", winner=loud)

        self.valorant_crud.create_game(loud_nrg1)
        self.valorant_crud.create_game(loud_nrg2)
        self.valorant_crud.create_game(loud_nrg3)
