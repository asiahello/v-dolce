import enum

import settings
from characters import Deck, Player, Fortniter


class TurnStage(int, enum.Enum):
    DRAW = 0
    FIGHT = 1
    END = 2


class SleepTime(int, enum.Enum):
    DRAW = 1000
    FIGHT = 2000
    END = 2000

class FortniteWarEngine:
    def __init__(self):
        self.players = Player.create_players()
        self.deck = Deck()

        # self.current_player = 0
        self.turn_stage = TurnStage.DRAW

    # def switch_player(self):
    #     self.current_player = (self.current_player + 1) % settings.NUM_PLAYERS
    #
    # def draw(self):
    #     self.players[self.current_player].hand = self.deck.deal()

    def switch_turn(self):
        if self.turn_stage == TurnStage.FIGHT:
            self.turn_stage = TurnStage.DRAW
            return

        if self.turn_stage == TurnStage.DRAW:
            self.turn_stage = TurnStage.FIGHT
            return

    def get_sleep_time(self):
        return SleepTime[self.turn_stage.name]

    def draw_for_all(self):
        for player in self.players:
            player.hand = self.deck.deal()

    def hit_looser(self):
        looser = min([player for player in self.players], key=lambda x: x.hand.damage)
        print([player.hand.damage for player in self.players])
        looser.health_points -= looser.hand.damage

    def get_winner(self):
        return max([player for player in self.players], key=lambda x: x.health_points)

    def check_end(self):
        if any(player.health_points <= 0 for player in self.players):
            self.turn_stage = TurnStage.END

    def play(self):
        if self.turn_stage == TurnStage.END:
            return

        if self.turn_stage == TurnStage.DRAW:
            self.draw_for_all()

        elif self.turn_stage == TurnStage.FIGHT:
            self.hit_looser()
            self.check_end()
