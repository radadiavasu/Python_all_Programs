from database import Database


class Saveble:
    def save(self):
        Database.insert(self.to_dict())