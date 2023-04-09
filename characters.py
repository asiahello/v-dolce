import os

import pygame
import random
import settings


class Player:
    def __init__(self, name):
        self.name = name
        self.health_points = settings.MAX_HEALTH
        self.hand = None

    def __str__(self):
        return f"{self.name}: {self.health_points} HP, {self.hand}"

    @classmethod
    def create_players(cls):
        return [cls(f"Player {i}") for i in range(settings.NUM_PLAYERS)]


class Fortniter:
    def __init__(self, asset_name: str, rarity: int = 0) -> None:
        self.image = pygame.image.load(f"assets/{asset_name}")
        self.name, self.damage = self.parse_asset_name(asset_name)
        self.rarity = rarity

    def __str__(self):
        return f"{self.name}, damage: {self.damage}"

    @classmethod
    def create_fortniters_from_assets(cls):
        return [cls(path) for path in os.listdir('assets') if path.endswith('.jpg')]

    @staticmethod
    def parse_asset_name(asset_name: str) -> tuple:
        name_and_damage = asset_name.split('.')[0]
        try:
            name, damage = name_and_damage.rsplit(' ', 1)
        except ValueError:
            name, damage = name_and_damage, 0
        return name, int(damage)


class Deck:
    def __init__(self):
        self.fortniters = Fortniter.create_fortniters_from_assets()
        self.cards = self.fortniters.copy()
        self.shuffle()

    @property
    def length(self):
        return len(self.cards)

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self):
        try:
            return self.cards.pop()
        except IndexError:
            print("Deck is empty. Reshuffling.")
            self.cards = self.fortniters.copy()
            self.shuffle()
            return self.cards.pop()

