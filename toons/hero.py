class Hero:
    def __init__(self, x=255, y=240):
        self.x = x
        self.y = y
        self.speed_x = 0
        self.speed_y = 0

    def move(self):
        new_x = self.x + self.speed_x
        new_y = self.y + self.speed_y
        if 25 < new_x < 450:
            self.x = new_x
        if 25 < new_y < 420:
            self.y = new_y
