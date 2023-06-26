from bson.objectid import ObjectId


class Player:
    def __init__(self, player_id: [str, None], name: str, nationality: str):
        if not player_id:
            self.id = str(ObjectId())
        else:
            self.id = player_id
        self.name = name
        self.nationality = nationality

    def get_id(self) -> str:
        return self.id

    def get_name(self):
        return self.name

    def set_name(self, new_name: str) -> None:
        self.name = new_name
        return None

    def get_nationality(self):
        return self.nationality

    def set_nationality(self, new_nationality: str) -> None:
        self.nationality = new_nationality
        return None

    def show_stats(self):
        print(f"name: {self.get_name()} | nationality: {self.get_nationality()} | id: {self.get_id()}")
        return None

    def asDict(self):
        dictionary = self.__dict__
        return dictionary
