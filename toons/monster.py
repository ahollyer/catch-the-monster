import random

class Monster:
        def __init__(
            self, pos=[30, 25], speed_x=0, speed_y=0,
            change_dir_countdown=60, alive=True, width=0, height=0
            ):
            self.pos = pos
            self.speed_x = speed_x
            self.speed_y = speed_y
            self.change_dir_countdown = change_dir_countdown
            self.alive = alive
            self.width = width
            self.height = height

        def wrap(self):
            if self.pos[0] > self.width:
                self.pos[0] = 0
            elif self.pos[0] < 0:
                self.pos[0] = self.width
            elif self.pos[1] > self.height:
                self.pos[1] = 0
            elif self.pos[1] < 0:
                self.pos[1] = self.height

        def move(self):
            self.pos[0] += self.speed_x
            self.pos[1] += self.speed_y
            return [self.pos[0], self.pos[1]]

        def change_dir(self):
            self.change_dir_countdown -= 1
            if self.change_dir_countdown == 0:
                self.speed_x = random.randint(-5, 5)
                self.speed_y = random.randint(-5, 5)
                self.change_dir_countdown = 60
