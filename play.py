import pygame
import random

def main():
    width = 512
    height = 480
    blue_color = (97, 159, 182)

    # sprite postitioning/movement
    x = 0
    y = 1
    speed_x = 3
    speed_y = -3
    change_dir_countdown = 60

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('My Game')
    clock = pygame.time.Clock()

    # Game initialization
    background_image = pygame.image.load(
        'images/background.png').convert_alpha()
    hero = pygame.image.load('images/hero.png')
    monster = pygame.image.load('images/monster.png')
    monster_pos = [30, 25]

    stop_game = False
    while not stop_game:
        for event in pygame.event.get():

            # Event handling

            if event.type == pygame.QUIT:
                stop_game = True


        # Game logic
        def wrap_monster():
            if monster_pos[x] > width:
                monster_pos[x] = 0
            elif monster_pos[x] < 0:
                monster_pos[x] = width
            elif monster_pos[y] > height:
                monster_pos[y] = 0
            elif monster_pos[y] < 0:
                monster_pos[y] = height

        wrap_monster()
        monster_pos[x] += speed_x
        monster_pos[y] += speed_y

        change_dir_countdown -= 1
        if change_dir_countdown == 0:
            speed_x = random.randint(-5, 5)
            speed_y = random.randint(-5, 5)
            change_dir_countdown = 60


        # Draw background
        screen.fill(blue_color)

        # Game display
        screen.blit(background_image, (0, 0))
        screen.blit(hero, (250, 240))
        print(monster_pos)
        screen.blit(monster, (monster_pos[x], monster_pos[y]))
        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
