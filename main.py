import pygame
import settings
from engine import FortniteWarEngine, TurnStage


pygame.init()
screen = pygame.display.set_mode(settings.BOUNDS)
pygame.display.set_caption("Fortnite War")

game_engine = FortniteWarEngine()


def render_game(screen):
    screen.fill(settings.BACKGROUND_COLOR)
    font = pygame.font.SysFont('comicsans', 60, True)

    for number, player in enumerate(game_engine.players):
        text = font.render(f"{player.name}: {player.health_points} HP", True, (255, 255, 255))
        player_origin = settings.PLAYER_ORIGINS[number]
        screen.blit(text, player_origin)

    if game_engine.turn_stage == TurnStage.DRAW:
        text = font.render("Dobieranie", True, (255, 255, 255))
        screen.blit(text, settings.MIDDLE_ORIGIN)

    if game_engine.turn_stage == TurnStage.FIGHT:
        text = font.render("Walka", True, (255, 255, 255))
        screen.blit(text, settings.MIDDLE_ORIGIN)

        for number, player in enumerate(game_engine.players):
            hand_origin = settings.HAND_ORIGINS[number]
            screen.blit(player.hand.image, hand_origin)


    if game_engine.turn_stage == TurnStage.END:
        message = "Game Over! " + game_engine.get_winner().name + " wins!"
        text = font.render(message, True, (255, 255, 255))
        screen.blit(text, settings.MIDDLE_ORIGIN)


running = True
while running:
    for event in pygame.event.get():
        key = None
        if event.type == pygame.QUIT:
            running = False
        # if event.type == pygame.KEYDOWN:
        #     key = event.key

    game_engine.play()
    render_game(screen)
    pygame.display.update()
    game_engine.switch_turn()
    pygame.time.wait(game_engine.get_sleep_time())


pygame.quit()


