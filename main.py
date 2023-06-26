from valorant_CLI import ValorantCLI
from database import Database
from valorant_CRUD import ValorantCRUD

# configurando o banco de dados
db = Database("bolt://44.199.233.191:7687", "neo4j", "verb-total-guests")
db.drop_all()
valorant_crud = ValorantCRUD(db)

# iniciando o app
valorant_cli = ValorantCLI(valorant_crud)
valorant_cli.start()
