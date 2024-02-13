from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player, x, y, speed, width, height):
        super().__init__()
        self.player = transform.scale(image.load(player), (width, height))
        self.speed = speed
        self.rect = self.player.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        my_win.blit(self.player, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 500 - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 500 - 80:
            self.rect.y += self.speed
ball = GameSprite('ball.png', 350, 250, 10, 50, 50)
player1 = Player('racket.png', 5, 170, 10, 50, 100)
player2 = Player('racket.png', 645, 170, 10, 50, 100)

bg = (200, 200, 255)
my_win = display.set_mode((700, 500))
my_win.fill(bg)


clock = time.Clock()
run = True
finish = False
speed_x = 3
speed_y = 3
font.init()
font = font.Font(None, 100)
win_player1 = font.render('Player 1 wins!', True, (0, 150, 0))
win_player2 = font.render('Player 2 wins!', True, (0, 150, 0))
while run:
    for i in event.get():
        if i.type == QUIT:
            run = False
    if not finish:
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        my_win.fill(bg)
        player1.update_l()
        player1.reset()
        player2.update_r()
        player2.reset()
        ball.reset()
        if ball.rect.y > 450 or ball.rect.y < 0:
            speed_y *= -1
        if sprite.collide_rect(ball, player1) or sprite.collide_rect(ball, player2):
            speed_x *= -1
            speed_y *= -1
        if ball.rect.x > 650:
            finish = True
            my_win.blit(win_player1, (120, 220))
        if ball.rect.x < 0:
            finish = True
            my_win.blit(win_player2, (120, 220))
    display.update()
    clock.tick(60)