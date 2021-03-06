import pygame
import math

from toons.goblin import Goblin
from toons.hero import Hero
from toons.monster import Monster

KEY_UP = 273
KEY_DOWN = 274
KEY_LEFT = 276
KEY_RIGHT = 275
KEY_SPACE = 32

def main():
    width = 512
    height = 480

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('ThuggyKnight: Catch dat Monsta')
    clock = pygame.time.Clock()
    font = pygame.font.Font(None, 30)

    # Game initialization
    monster = Monster(width=width, height=height)
    goblin = Goblin(width=width, height=height)
    hero = Hero()

    background_image = pygame.image.load(
        'images/background.png').convert_alpha()
    goblin_sprite = pygame.image.load('images/goblin.png')
    hero_sprite = pygame.image.load('images/hero.png')
    monster_sprite = pygame.image.load('images/monster.png')
    win_sound = pygame.mixer.Sound('sounds/win.wav')
    win_text = font.render('You win! Hit SPACE to play again.', False, (0, 0, 0))
    lose_sound = pygame.mixer.Sound('sounds/lose.wav')
    lose_text = font.render('Haha you suck. Hit SPACE to play again.', False, (255, 0, 0))

    stop_game = False
    game_won = False
    game_lost = False
    while not stop_game:
        for event in pygame.event.get():

            # Hero movement controls
            if event.type == pygame.KEYDOWN:
                # activate the corresponding speeds
                # when an arrow key is pressed down
                if event.key == KEY_DOWN:
                    hero.speed_y = 5
                elif event.key == KEY_UP:
                    hero.speed_y = -5
                elif event.key == KEY_LEFT:
                    hero.speed_x = -5
                elif event.key == KEY_RIGHT:
                    hero.speed_x = 5
            if event.type == pygame.KEYUP:
                # deactivate the cooresponding speeds
                # when an arrow key is released
                if event.key == KEY_DOWN:
                    hero.speed_y = 0
                elif event.key == KEY_UP:
                    hero.speed_y = 0
                elif event.key == KEY_LEFT:
                    hero.speed_x = 0
                elif event.key == KEY_RIGHT:
                    hero.speed_x = 0

            # Click X to quit
            if event.type == pygame.QUIT:
                stop_game = True

            # Use enter to start new game after winning
            if game_won:
                if event.type == pygame.KEYUP:
                    if event.key == KEY_SPACE:
                        main()


        # Game logic
        monster.wrap()
        monster.change_dir()
        monster.move()

        goblin.wrap()
        goblin.change_dir()
        goblin.move()

        hero.move()

        # Check positions of sprites
        goblin_collision_test = math.sqrt((hero.x - goblin.pos[0])**2 + (hero.y - goblin.pos[1])**2)

        if goblin_collision_test < 32:
            game_lost = True


        monster_collision_test = math.sqrt((hero.x - monster.pos[0])**2 + (hero.y - monster.pos[1])**2)

        if monster_collision_test < 32:
            game_won = True

        if game_won:
            monster.alive = False

        # Game display
        screen.blit(background_image, (0, 0))
        screen.blit(hero_sprite, (hero.x, hero.y))
        screen.blit(goblin_sprite, (goblin.pos[0], goblin.pos[1]))
        if monster.alive:
            screen.blit(monster_sprite, (monster.pos[0], monster.pos[1]))
        if game_won:
            win_sound.play()
            screen.blit(win_text, (150, 200))
        if game_lost:
            lose_sound.play()
            screen.blit(lose_text, (80, 200))
        pygame.display.update()
        clock.tick(60)

    pygame.quit()


if __name__ == '__main__':
    main()
