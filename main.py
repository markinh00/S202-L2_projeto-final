from player import Player
from team import Team
from database import Database
from valorant_crud import Valorant

db = Database(database="S202-L2_EA2", collections=["players", "teams", "matches"])
db.resetDatabase()
valorant_db = Valorant(db)

loud_list = [Player(player_id=None, name="aspas", nationality="Brasil"),
             Player(player_id=None, name="saadhak", nationality="Argentina"),
             Player(player_id=None, name="tuyz", nationality="Brasil"),
             Player(player_id=None, name="less", nationality="Brasil"),
             Player(player_id=None, name="cauanzin", nationality="Brasil")]
loud = Team(team_id=None, name="Loud", list_of_players=loud_list)

nrg_list = [Player(player_id=None, name="FINESSE", nationality="Canada"),
            Player(player_id=None, name="s0m", nationality="USA"),
            Player(player_id=None, name="crashies", nationality="USA"),
            Player(player_id=None, name="ardiis", nationality="Latvia"),
            Player(player_id=None, name="Victor", nationality="USA")]
nrg = Team(team_id=None, name="NRG Esports", list_of_players=nrg_list)

eg_list = [Player(player_id=None, name="Boostio", nationality="USA"),
           Player(player_id=None, name="C0M", nationality="USA"),
           Player(player_id=None, name="jawgemo", nationality="Camboja"),
           Player(player_id=None, name="Ethan", nationality="USA"),
           Player(player_id=None, name="Demon1", nationality="USA")]
eg = Team(team_id=None, name="Evil Geniuses", list_of_players=eg_list)

c9_list = [Player(player_id=None, name="Zellsis", nationality="USA"),
           Player(player_id=None, name="Xeppaa", nationality="USA"),
           Player(player_id=None, name="leaf", nationality="USA"),
           Player(player_id=None, name="jakee", nationality="USA"),
           Player(player_id=None, name="runi", nationality="USA")]
c9 = Team(team_id=None, name="Cloud9", list_of_players=c9_list)

lev_list = [Player(player_id=None, name="nzr", nationality="Argentina"),
            Player(player_id=None, name="Tacolilla", nationality="Chile"),
            Player(player_id=None, name="Mazino", nationality="Chile"),
            Player(player_id=None, name="kiNgg", nationality="Chile"),
            Player(player_id=None, name="shyy", nationality="Chile")]
lev = Team(team_id=None, name="Leviatán", list_of_players=lev_list)

furia_list = [Player(player_id=None, name="mwzera", nationality="Brasil"),
              Player(player_id=None, name="Quick", nationality="Brasil"),
              Player(player_id=None, name="Khalil", nationality="Brasil"),
              Player(player_id=None, name="Mazin", nationality="Brasil"),
              Player(player_id=None, name="dgzin", nationality="Brasil")]
furia = Team(team_id=None, name="FURIA", list_of_players=furia_list)


