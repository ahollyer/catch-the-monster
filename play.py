import pygame
import math

from toons.monster import Monster
from toons.hero import Hero

KEY_UP = 273
KEY_DOWN = 274
KEY_LEFT = 276
KEY_RIGHT = 275

def main():
    width = 512
    height = 480

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('My Game')
    clock = pygame.time.Clock()

    # Game initialization
    monster = Monster(width=width, height=height)
    hero = Hero()

    background_image = pygame.image.load(
        'images/background.png').convert_alpha()
    hero_sprite = pygame.image.load('images/hero.png')
    monster_sprite = pygame.image.load('images/monster.png')

    stop_game = False
    game_won = False
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


        # Game logic
        monster.wrap()
        monster.change_dir()
        monster.move()

        # Check positions of hero/monster
        collision_test = math.sqrt((hero.x - monster.pos[0])**2 + (hero.y - monster.pos[1])**2)

        if collision_test < 32:
            game_won = True
        hero.move()

        if game_won:
            print("you won")


        # Game display
        screen.blit(background_image, (0, 0))
        screen.blit(hero_sprite, (hero.x, hero.y))
        screen.blit(monster_sprite, (monster.pos[0], monster.pos[1]))
        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
