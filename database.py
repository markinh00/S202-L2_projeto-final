import pymongo


class Database:
    def __init__(self, database: str, collections: list[str]):
        self.db = None
        self.collection = None
        self.clusterConnection = None
        self.collections = {}
        self.connect(database, collections)

    def connect(self, database, collections):
        try:
            connectionString = "localhost:27017"
            self.clusterConnection = pymongo.MongoClient(
                connectionString,
                tlsAllowInvalidCertificates=True
            )
            self.db = self.clusterConnection[database]
            for collection in collections:
                self.collections[collection] = (self.db[collection])
            print("Database connected successfully!")
        except Exception as e:
            print(e)

    def resetDatabase(self):
        try:
            for collection in self.collections:
                self.db.drop_collection(collection)
            print("Database reseted successfully!")
        except Exception as e:
            print(e)
