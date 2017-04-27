import pygame
import random

from toons.monster import Monster

def main():
    width = 512
    height = 480
    blue_color = (97, 159, 182)

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('My Game')
    clock = pygame.time.Clock()

    # Game initialization
    monster = Monster(width=width, height=height)

    background_image = pygame.image.load(
        'images/background.png').convert_alpha()
    hero_sprite = pygame.image.load('images/hero.png')
    monster_sprite = pygame.image.load('images/monster.png')

    stop_game = False
    while not stop_game:
        for event in pygame.event.get():

            # Event handling

            if event.type == pygame.QUIT:
                stop_game = True


        # Game logic

        monster.change_dir_countdown -= 1
        if monster.change_dir_countdown == 0:
            monster.speed_x = random.randint(-5, 5)
            monster.speed_y = random.randint(-5, 5)
            monster.change_dir_countdown = 60

        monster.wrap()
        monster.move()

        # Draw background
        screen.fill(blue_color)

        # Game display
        screen.blit(background_image, (0, 0))
        screen.blit(hero_sprite, (250, 240))
        screen.blit(monster_sprite, (monster.pos[0], monster.pos[1]))
        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
