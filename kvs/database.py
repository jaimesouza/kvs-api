from .model import KVSPair
from typing import List


class FakeDB:

    def __init__(self):
        self.db: List[KVSPair] = [
            KVSPair(key="id", value="ID001"),
            KVSPair(key="name", value="Jon Snow"),
            KVSPair(key="serie", value="Game of Thrones")
        ]

    def get_pairs(self):
        return self.db

    def insert(self, pair: KVSPair):
        self.db.append(pair)

    def get_pair_by_key(self, key: str):
        for pair in self.db:
            if pair.key == key:
                return pair
        return None

    def update(self, key: str, value: str):
        pair = self.get_pair_by_key(key)
        pair.value = value
        return pair

    def delete(self, key: str):
        pair = self.get_pair_by_key(key)
        self.db.remove(pair)
        return pair

    def key_exists(self, key: str):
        # check if the key exists in the database
        for pair in self.db:
            if pair.key == key:
                return True
        return False
